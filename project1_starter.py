"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Mariyah Curb
Date: 10/28/25

AI Usage: [Document any AI assistance used]
Ai (Copilot) automatically named and described almost all of my commits. 
used gemini to debug where my indentation errors
Use Chatgpt to debug broken functions (incorrect naming and improper use of variables)
"""
import os

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    """
    # Normalize class capitalization
    character_class = character_class.title()

    # Validate class
    valid_classes = {"Warrior", "Mage", "Rogue", "Cleric"}
    if character_class not in valid_classes:
        return None

    # Use calculate_stats so scaling logic is centralized
    strength, magic, health = calculate_stats(character_class, 1)

    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 250
    }
    return character



# Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 250}

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
def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    """
    base = {
        "Warrior": {"strength": 10, "magic": 2, "health": 15},
        "Mage":    {"strength": 3,  "magic": 10,"health": 8},
        "Rogue":   {"strength": 6,  "magic": 5, "health": 7},
        "Cleric":  {"strength": 5,  "magic": 8, "health": 12}
    }

    if character_class not in base:
        raise ValueError(f"Invalid class: {character_class}")

    base_stats = base[character_class]

    # Example scaling formula — adjust as you like
    scaled_strength = base_stats["strength"] + (level - 1) * 2
    scaled_magic   = base_stats["magic"]   + (level - 1) * 2
    scaled_health  = base_stats["health"]  + (level - 1) * 5

    return (int(scaled_strength), int(scaled_magic), int(scaled_health))
# TODO: Implement this function
# Return a tuple: (strength, magic, health)
pass

def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred (e.g. directory doesn't exist)
    """
    # If a directory is provided and it doesn't exist, return False rather than raising
    dirpath = os.path.dirname(filename)
    if dirpath and not os.path.exists(dirpath):
        return False

    # Write file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")

    return True
    
    
pass

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    if not os.path.exists(filename):
        return None

    character = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # split only on the first ": " in case values contain ":"
            parts = line.strip().split(": ", 1)
            if len(parts) != 2:
                continue
            key, value = parts
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)

    # If any required key missing, return None (or you could raise)
    required = ["name", "class", "level", "strength", "magic", "health", "gold"]
    if not all(k in character for k in required):
        return None

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
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
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
