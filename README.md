Murder Mystery Adventure
A classic text-based adventure game built with Python, where you step into the shoes of a detective to solve the murder of Sir Augustus. This project demonstrates core programming concepts, with a focus on clean, scalable code using Object-Oriented Programming (OOP) principles.

Synopsis
Welcome, Detective. You have been called to a stately manor to investigate the untimely death of Sir Augustus. The suspects—his son Duncan and the butler Justin—are being held in the lounge. It's up to you to explore the manor, gather all six clues, and piece together the puzzle. Your powers of deduction will be tested as you navigate through rooms, interact with objects, and ultimately, accuse the killer.

Features
Interactive World: Navigate between interconnected rooms using simple commands (north, south, east, west).

Item Collection: Discover and collect clues scattered throughout the manor.

Inventory Management: Keep track of the clues you've found with a dedicated inventory system.

Narrative Driven: A simple, engaging story that unfolds as you explore.

Multiple Endings: Your final accusation determines the outcome of the investigation.

Technical Design
This project was initially written as a procedural script and later refactored to use an Object-Oriented approach. This design separates the game's logic into distinct, reusable components, making the code more organized, readable, and easier to extend.

The architecture is built around four primary classes:

Core Classes
Game: The main engine that controls the game loop, processes user input, and manages the overall game state. It is responsible for setting up the game world and running the main loop.

Player: Represents the user. This class manages the player's current location within the game world and holds the inventory of collected clues (Item objects).

Room: Represents a single location in the game. Each Room object holds its own description, a dictionary of exits that link to other Room objects, and a collection of Item objects that can be found within it. This creates a graph of interconnected nodes that forms the game map.

Item: Represents a clue that can be found in a room and collected by the player. Each Item has a name and a detailed description.

This OOP structure ensures a clear separation of concerns, where each class has a single, well-defined responsibility.
