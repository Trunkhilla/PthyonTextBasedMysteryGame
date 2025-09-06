# Athena Trunkhill
# PythonTextBasedMysteryGame.py
# This is a text based mystery game.



class Item:
    """Represents an item (clue) in the game."""

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


class Room:
    """Represents a room in the game world."""

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}  # Mapping of direction -> Room object
        self.items = {}  # Mapping of item name -> Item object

    def add_exit(self, direction, room):
        """Adds an exit to the room."""
        self.exits[direction] = room

    def add_item(self, item):
        """Adds an item to the room."""
        self.items[item.name.lower()] = item

    def get_full_description(self):
        """Returns the full description of the room, including items."""
        full_desc = f"\n--- {self.name} ---\n{self.description}"
        if self.items:
            item_names = ", ".join(item.name for item in self.items.values())
            full_desc += f"\nYou notice the following: {item_names}."

        exit_names = ", ".join(self.exits.keys())
        full_desc += f"\nExits are: {exit_names.title()}."
        return full_desc


class Player:
    """Represents the player."""

    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def take_item(self, item):
        """Adds an item to the player's inventory."""
        self.inventory.append(item)
        print(f"\nYou take the suspicious {item.name} and add it to your Inventory.")
        print(f'"{item.description}"')

    def show_inventory(self):
        """Prints the player's inventory."""
        if not self.inventory:
            print("\nYour inventory is empty.")
        else:
            print("\n--- Inventory ---")
            for item in self.inventory:
                print(f"- {item.name}")
            print("-----------------")


class Game:
    """The main game engine."""

    def __init__(self):
        self.player = None
        self.all_clues = []
        self._setup_game()
        self.game_over = False

    def _setup_game(self):
        """Creates all rooms, items, and the player."""
        # --- Create Items (Clues) ---
        clues_data = {
            'Letter': 'This appears to be a threatening letter written in a Red Ink signed Duncan.',
            'Red Ink Vial': 'This is an almost empty vial of Red Ink.',
            'Police Report': 'This Report outlines that Sir Augustus died of poisoning and not the stab wound found on the body.',
            'Crumpled Note': 'This appears to be a Shopping List with "Eggs, Milk, and Sleeping Pills" listed.',
            'Bloody Knife': 'This Bloody Knife seemed carelessly hidden, could it be connected to the murder?',
            'Handkerchief': 'This Handkerchief has the letter "J" embroidered on it.'
        }
        items = {name: Item(name, desc) for name, desc in clues_data.items()}
        self.all_clues = list(items.values())

        # --- Create Rooms ---
        rooms = {
            'foyer': Room('Foyer', 'You are in the house Foyer with a fellow detective.'),
            'study': Room('Study', 'You are in the Study with a white outline of a body on the floor.'),
            'hallway': Room('Hallway',
                            'You find yourself in a well decorated hallway. A large painting of a cow hangs over a small table.'),
            'masterbedroom': Room('Master Bedroom',
                                  'You are in what looks like an elegant bedroom. There is a neatly made up bed and a desk.'),
            'guestbedroom': Room('Guest Bedroom', 'You are in a small bedroom.'),
            'walkincloset': Room('Walk in Closet', 'You are in a closet with several jackets and boots.'),
            'supplycloset': Room('Supply Closet',
                                 'You are in a cramped closet full of cleaning supplies that seems to be used by the butler.'),
            'lounge': Room('Lounge',
                           'You see Duncan and Justin sitting on opposite ends of the room. They both look nervous.')
        }

        # --- Add Items to Rooms ---
        rooms['masterbedroom'].add_item(items['Letter'])
        rooms['supplycloset'].add_item(items['Red Ink Vial'])
        rooms['hallway'].add_item(items['Police Report'])
        rooms['guestbedroom'].add_item(items['Crumpled Note'])
        rooms['walkincloset'].add_item(items['Bloody Knife'])
        rooms['study'].add_item(items['Handkerchief'])

        # --- Link Rooms Together ---
        rooms['foyer'].add_exit('north', rooms['study'])
        rooms['foyer'].add_exit('west', rooms['hallway'])

        rooms['study'].add_exit('south', rooms['foyer'])
        rooms['study'].add_exit('north', rooms['lounge'])

        rooms['hallway'].add_exit('east', rooms['foyer'])
        rooms['hallway'].add_exit('north', rooms['masterbedroom'])
        rooms['hallway'].add_exit('south', rooms['guestbedroom'])
        rooms['hallway'].add_exit('west', rooms['supplycloset'])

        rooms['masterbedroom'].add_exit('south', rooms['hallway'])

        rooms['guestbedroom'].add_exit('north', rooms['hallway'])
        rooms['guestbedroom'].add_exit('west', rooms['walkincloset'])

        rooms['walkincloset'].add_exit('east', rooms['guestbedroom'])

        rooms['supplycloset'].add_exit('east', rooms['hallway'])

        rooms['lounge'].add_exit('south', rooms['study'])  # Not a real exit, just for structure

        # --- Create Player ---
        self.player = Player(rooms['foyer'])

    def _show_intro(self):
        """Displays the game's introduction."""
        print("--- Murder Mystery Text Adventure Game ---")
        print(self.player.current_room.get_full_description())
        print('\nAh, welcome Detective. Come to help solve the murder of Sir Augustus?\n....')
        print('Perfect! We have all Suspects in the Lounge which is to the North of the Study.')
        print('\nI will keep this room secure and you can go around the house checking for any clues.')
        print('\n--- How to Play ---')
        print('* Move by typing a direction: "north", "south", "east", or "west".')
        print('* Interact with items by typing their name (e.g., "Letter").')
        print('* Type "inventory" to see your collected clues.')
        print('* Type "look" to see the room description again.')
        print('* Type "quit" to leave the game early.')
        print('--------------------')

        while True:
            intro_clue = input(
                'Every detective needs their trusty "Magnifying Glass". Try typing that in now to take mine: ')
            if intro_clue.lower() == 'magnifying glass':
                print('\nFantastic! Now you should be able to find those clues!')
                print('Remember, there should be 6 clues scattered around the house.')
                print("Make sure you do not enter the Lounge until after you find all the clues.")
                print("That is where we are holding the suspects; Sir Augustus's son Duncan and his Butler Justin.")
                break
            else:
                print("That's not it. Try again.")

    def run(self):
        """Starts and runs the main game loop."""
        self._show_intro()

        while not self.game_over:
            print(self.player.current_room.get_full_description())
            self._process_command()

        print("\nThanks for playing!")

    def _process_command(self):
        """Gets and processes a command from the user."""
        action = input('\nWhat would you like to do?: ').lower().strip()

        # Movement commands
        if action in ['north', 'south', 'east', 'west']:
            self._move(action)
        # Other commands
        elif action == 'inventory':
            self.player.show_inventory()
        elif action == 'look':
            # The room description is already printed at the start of the loop
            pass
        elif action == 'quit':
            self.game_over = True
            print("You decide to leave the case for another day.")
        # Item interaction
        elif action in self.player.current_room.items:
            self._take(action)
        else:
            print("\nPlease enter a valid command or item name.")

    def _move(self, direction):
        """Handles player movement."""
        if direction in self.player.current_room.exits:
            next_room = self.player.current_room.exits[direction]

            # Special condition for entering the lounge
            if next_room.name == 'Lounge':
                if len(self.player.inventory) == len(self.all_clues):
                    print("\nYou have all the clues. It's time to face the suspects.")
                    self.player.current_room = next_room
                    self._handle_accusation()
                else:
                    print("\nYou feel you aren't ready to enter the lounge yet. You need all 6 clues first.")
            else:
                self.player.current_room = next_room
        else:
            print("\nYou can't go that way.")

    def _take(self, item_name):
        """Handles taking an item."""
        item = self.player.current_room.items.pop(item_name)
        self.player.take_item(item)

    def _handle_accusation(self):
        """Handles the final accusation sequence."""
        print(f"\n--- {self.player.current_room.name} ---")
        print(self.player.current_room.description)
        print('\nThe Detective enters the room from behind you.')
        print('Ah, I see you have found all of the clues you needed?')
        print(
            'So you discovered; a Letter, a Red Ink Vial, the Police Report, a Crumpled Note, a Bloody Knife, and a Handkerchief?')
        print('Well in that case, what do you make of all of it?')

        while True:
            accused = input('\nDo you think it was "Justin" or "Duncan" who killed him?: ').lower().strip()
            if accused == 'duncan':
                print('\nDuncan? Yes that could be... ')
                print('Duncan could have written the threatening note and put the Red Ink inside the supply '
                      'closet to frame the Butler. \nIn addition, perhaps the Sleeping Pills on this Crumpled Note could have been to murder his father!')
                print('...But why would he have hidden the Bloody Knife in his own closet? ')
                print(
                    'And the Handkerchief at the crime scene does not make sense either... as well signing his own name to the note...')
                print('\nOh well that is for the courts to decide the important thing is you gathered all these clues!')
                print('\nThank you for your hard work and congratulations!')
                break
            elif accused == 'justin':
                print('\nJustin? Yes that could be... ')
                print(
                    'Justin could have written the threatening note and signed it as Duncan to frame him, the Red Ink was with his stuff after all! ')
                print('The Red Ink does not match the writing on this Crumpled Note you found from Duncan either. ')
                print(
                    'In addition we know that Sir Augustus was killed by poison and not from a stab wound from the Police Report... \nSo the Bloody Knife makes no sense to be in the closet unless it too was put their to frame Duncan! ')
                print('Finally, this Handkerchief at the scene of the crime has a "J" and NOT a "D" on it.')
                print('\nI do believe you have solved the case!!!')
                print('\nThank you for your hard work uncovering the true killer and congratulations!')
                break
            else:
                print('I did not quite catch that, could you speak up?')

        self.game_over = True


# This ensures the game only runs when the script is executed directly
if __name__ == "__main__":
    game = Game()
    game.run()