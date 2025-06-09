# **Bedtime Adventure Text Game**

**Overview**
The Bedtime Adventure text-based dungeon crawler was created with Python. In this game, you play as a tired parent trying to collect all the necessary bedtime items to lure their baby to sleep.

**Gameplay**
- Navigate through various rooms in the house: Living Room, Dining Room, Kitchen, Play Room, Laundry Room, Bedroom One, Bedroom Two, and Bathroom.
- Collect six essential bedtime items: pajamas, book, bottle, pacifier, blanket, and teddy bear.
- The baby, the game's villain, is located in the Laundry Room.
- If you enter the Laundry Room before gathering all items, the baby refuses to sleep and you lose.
- If you collect all six items before meeting the baby, you win.

**Controls**
- Move commands: North, South, East, West
- When prompted, choose whether to take an item with: Yes or No
- To exit the game at any time, type Exit

**How It Works**
- The player starts in the Living Room with an empty inventory.
- Each move updates your current room and inventory.
- Rooms are connected via directional moves stored in a dictionary.
- Items are linked to specific rooms.
- Collect items to progress and ultimately soothe the baby.

**Sample Interaction**

![DungeonCrawler](https://github.com/user-attachments/assets/cfb6a3c8-fbef-4925-8f38-30798bc7f193)

**Future Improvements**
- Add input validation to accept uppercase/lowercase and prevent invalid commands.
- Enhance gameplay with additional story elements or timed challenges.
- Include a graphical interface for better user experience.
