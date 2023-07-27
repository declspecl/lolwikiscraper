import json
from champion import Champion, ChampionEncoder, ChampionDecoder

def export_with_format(champions: list[Champion], filename: str, format: str) -> bool:
    """
    Exports the champions list into a file with a supplied format string to dictate how the data will be exported

    # Parameters:
    - champions (list[Champion]): The list of champion objects to be exported
    - filename (str): The name of the file the data will be written to. Include the file extension in the filename.
    - format (str): A string to dictate how each line of data for each champion will be written. See the explanation below

    # Format:
    There are many different delimeters to dictate the format of the lines exported into the csv file

    ## Champion delimeters
    A Champion object has 2 members, but the abilities have their own delimeters, so only the name member will receive one:
    - {N} / {n}: Insert these 3 characters to place the champion's name here, use {n} for all lowercase
    
    ## Ability delimeters
    IMPORTANT: These delimeters can ONLY be present between [square brackets], as the square brackets define how each ability should be formatted
    An Ability object has 3 members, so 3 delimeters will be supplied:
    - (N) / (n): Insert these 3 characters to place the ability's name here
    - (S) / (s): Insert these 3 characters to place the ability's slot here
    - (C) / (c): Insert these 3 characters to place the ability's cooldowns here

    The abilities will be printed in Passive -> Q -> W -> E -> R -> Other precedence

    ## Other delimeters
    Wrap a group of characters around your ability delimeter with [square brackets] to denote how the format should be for EACH ability
    Every delimeter that Python supports can also be included including but not limited to:
    - '\\n'
    - '\\t'

    ## Examples
    A format of "{N}:\\n[\\t(S): (N) @ (C)\\n]" outputs (for one champion):
    ```
    Riven:
        Passive: Runic Blade @ None
        Q: Broken Wings @ [13]
        W: Ki Burst @ [11, 10, 9, 8, 7]
        E: Valor @ [10, 9, 8, 7, 6]
        R: Blade of the Exile @ [120, 90, 60]
    ```

    A format of "# {n}\\n## cds\\n[- (s): (c)\\n]\\n" outputs (for one champion):
    ```
    # riven
    ## cds
    - passive: none
    - q: 13
    - w: [11, 10, 9, 8, 7]
    - e: [10, 9, 8, 7, 6]
    - r: [120, 90, 60]
    ```

    # Returns:
    - bool: True if the operation suceeded, otherwise False
    """

    if (ability_format_start := format.find("[")) + (ability_format_end := format.find("]")) == -2:
        print("You must include [square brackets] around a region of the format string to denote how to format each ability")
        return False
    
    prefix_format: str = format[:ability_format_start]
    ability_format: str = format[ability_format_start + 1 : ability_format_end]
    suffix_format: str = format[ability_format_end + 1:]

 
    with open(f".\\{filename}", "w", encoding="utf-8") as file:
        for champion in champions:
            formatted_line: str = prefix_format.replace("{N}", champion.name).replace("{n}", champion.name.lower())

            for ability in champion.abilities:
                formatted_line += ability_format \
                    .replace("\u2212", "-") \
                    .replace("(N)", ability.name) \
                    .replace("(n)", ability.name.lower()) \
                    .replace("(S)", ability.slot.name.capitalize()) \
                    .replace("(s)", ability.slot.name.lower()) \
                    .replace("(C)", " / ".join(map(lambda x: str(x), ability.cooldowns)) if isinstance(ability.cooldowns, list) else str(ability.cooldowns)) \
                    .replace("(c)", " / ".join(map(lambda x: str(x), ability.cooldowns)).lower() if isinstance(ability.cooldowns, list) else str(ability.cooldowns).lower())
                
            formatted_line += suffix_format.replace("{N}", champion.name)

            print(formatted_line)
            file.write(formatted_line)

        return True

def export_to_json(champions: list[Champion], filename: str, indent: int = None) -> bool:
    """
    Exports the champions list into a file in JSON format

    # Parameters:
    - champions (list[Champion]): The list of champion objects to be exported
    - filename (str): The name of the file the data will be written to. Include the file extension in the filename.
    - indent (int): An integer representing the desired amount of spaces to indent each new block

    # Returns:
    - bool: True if the operation suceeded, otherwise False
    """
    try:
        with open(".\\{}.json".format(filename if not filename.endswith(".json") else filename[:filename.rfind(".")]), "w", encoding="utf-8") as file:
            file.write(json.dumps(champions, cls=ChampionEncoder, indent=indent))

        return True
    
    except Exception as e:
        print(e)
        return False

def import_from_json(filename: str) -> list[Champion]:
    """
    Returns the list of Champion objects from the supplied JSON file (to avoid re-scraping the website)
    
    # Parameters:
    - filename (str): The name/path of the file (include the extension)

    # Returns:
    - list[Champion]: The list of Champion objects
    """
    with open(f".\\{filename}", "r") as file:
        return json.load(file, cls=ChampionDecoder)