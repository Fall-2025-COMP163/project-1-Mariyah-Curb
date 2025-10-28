"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Mariyah Curb
Date: 10/28/25

AI Usage: [Document any AI assistance used]
Ai (Copilot) automatically named and described almost all of my commits. 
used gemini to debug where my indentation errors
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold

    Example:
    char = create_character("Aria", "Mage")
    # Create dictionary for the base stats of a chracter depending on class
    """

    base_stats = {
        "Warrior": {"strength": 10, "magic": 2, "health": 15}, # 27
        "Mage": {"strength": 3, "magic": 10, "health": 8}, # 21
        "Rogue": {"strength": 6, "magic": 5, "health": 7}, # 18
        "Cleric": {"strength": 5, "magic": 8, "health": 12} # 25
    }
    # The rogue sucks and warrior too op number noted for possible rebalancing 
    stats = base_stats[character_class]

    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": stats["strength"],
        "magic": stats["magic"],
        "health": stats["health"],
        "gold": 250
    }
    return character



# Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}

# Remember to use calculate_stats() function for stat calculation
pass
"""
def calculate_stats(character_class, level):


Calculates base stats based on class and level
Returns: tuple of (strength, magic, health)

Design your own formulas! Ideas:
- Warriors: High strength, low magic, high health
- Mages: Low strength, high magic, medium health  
- Rogues: Medium strength, medium magic, low health
- Clerics: Medium strength, high magic, high health
"""

#store the character stats then use them to calculate over level/ data
def calculated_stats(character_class, level):
    base = {
    "Warrior": {"strength": 10, "magic": 2, "health": 15},
    "Mage": {"strength": 3, "magic": 10, "health": 8},
    "Rogue": {"strength": 6, "magic": 5, "health": 7},
    "Cleric": {"strength": 5, "magic": 8, "health": 12}
    }
    base_stats = base[character_class]

    scaled_stats = {
        "strength": base_stats["strength"] + (level - 1) * 2,
        "magic": base_stats["magic"] + (level - 1) * 2,
        "health": base_stats["health"] + (level - 1) * 5
    }

    return scaled_stats
# TODO: Implement this function
# Return a tuple: (strength, magic, health)
pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred

    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    with open(filename, "w") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    
pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    character = {}
    with open(filename, "r") as file:
        for line in file:
            key, value = line.strip().split(": ")
    return {
        "name": character["name"],
        "class": character["class"],
        "level": character["level"],
        "strength": character["strength"],
        "magic": character["magic"],
        "health": character["health"],
        "gold": character["gold"]
    }
# TODO: Implement this function
# Remember to handle file not found errors
pass

def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)

    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print(f"\n=== CHARACTER SUMMARY ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("==========================\n")
# doesnt need to return anything
pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    character["level"] += 1
    updated = calculated_stats(character["class"], character["level"])
    character.update(updated)
    character["gold"] += 50  # reward for leveling up

    return character
pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
    name = input("Enter your character's name: ").strip()
    print("Choose a class: Warrior, Mage, Rogue, or Cleric")
    char_class = input("Enter class: ").strip().title()

    char = create_character(name, char_class)
    display_character(char)

    save_character(char, "saved_character.txt")
    print("Character saved!")

    print("Leveling up...")
    char = level_up(char)
    display_character(char)

    save_character(char, "saved_character.txt")
    print("Updated character saved again.")
"""
Errors That were in my code

Indentation Errors causing nested loops and regular loops to run incorrectly
Bro the indentations were so bad i had to rerun in visual studios to fix the erros so they were highlighted
"""
