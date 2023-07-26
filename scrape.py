import requests
from bs4 import BeautifulSoup, Tag

from champion import Champion
from ability import Ability, AbilitySlot

def get_champion(champ_name: str, verbose: bool = False) -> Champion:
    """
    Returns a Champion object representing the champion with the given name

    Parameters:
    - champ_name (str): The name of the champion that you want to get the Champion object of
    - verbose (bool): Choose whether to print the real time progress of the scraper

    Returns:
    - Champion: The Champion object of the champion with the given name
    """

    if verbose:
        print("{}:".format(champ_name))

    return Champion(champ_name, get_champion_abilities(champ_name, verbose))

def get_champion_abilities(champ_name: str, verbose: bool = False) -> list[Ability]:
    """
    Returns a list of the abilities of a champion given the champion's name

    Parameters:
    - champ_name (str): The name of the champion that you want to get the abilities of
    - verbose (bool): Choose whether to print the real time progress of the scraper

    Returns:
    - list[Ability]: A list of all the champion's abilities
    """

    # getting data from wiki post of champion
    champion_url: str = "https://leagueoflegends.fandom.com/wiki/{}/LoL".format(champ_name)
    res = requests.get(champion_url)

    # setting up parser
    soup = BeautifulSoup(res.content, "html.parser")

    # finding every element with the class "skill" (each ability)
    ability_tags: list[Tag] = soup.find_all(class_="skill")

    abilities: list[Ability] = []

    # adding every ability
    for tag in ability_tags:
        # avoiding samira's /taunt
        if len(tag["class"]) <= 1:
            continue

        ability_name: str = tag.find(class_="mw-headline").text

        if verbose:
            print("\t- {}".format(ability_name))

        ability_slot: AbilitySlot = AbilitySlot.class_to_abilityslot(tag["class"][1])
        ability_cooldowns: list[int] | str | None = None

        ability_cooldown_tag: Tag | None = tag.find(attrs={"data-source": "cooldown"})

        if ability_cooldown_tag != None:
            try:
                ability_cooldown_text: str = ability_cooldown_tag.find(class_="pi-data-value").text.strip()

                ability_cooldowns = [ int(cooldown) for cooldown in ability_cooldown_text.split(" / ") ]
            except:
                ability_cooldowns = ability_cooldown_text
        else:
            ability_cooldowns = None

        abilities.append(
            Ability(
                ability_name,
                ability_slot,
                ability_cooldowns
            )
        )

    if verbose:
        print()

    return abilities

def get_all_champions(verbose: bool = False) -> list[Champion]:
    """
    Returns all champions as a list.

    Use this function INSTEAD OF get_all_champions_as_dictionary if you prefer a list. Calling both will rescrape the entire website.

    Parameters:
    - verbose (bool): Choose whether to print the real time progress of the scraper

    Returns:
    - list[Champion]: A list of all Champion objects
    """

    # getting data from list of champs wiki post
    champion_list_url: str = "https://leagueoflegends.fandom.com/wiki/List_of_champions"
    res = requests.get(champion_list_url)

    # setting up parser
    soup = BeautifulSoup(res.content, "html.parser")

    # getting the table of champs
    champ_table: Tag = soup.find("table", class_="article-table")

    # accessing the data-champion attribute value for every champion row in the table and making Champion objects from it
    champions: list[Champion] = []

    for champ_tag in champ_table.find_all(attrs={"data-champion": True}):
        if verbose:
            print("{}:".format(champ_tag["data-champion"]))

        champions.append(Champion(champ_tag["data-champion"], get_champion_abilities(champ_tag["data-champion"], verbose)))

    return champions

#
def get_all_champions_as_dictionary(verbose: bool = False) -> dict[str, Champion]:
    """
    Returns all champions in a dictionary where the key is the name and the value is the Champion object.

    Use this function INSTEAD OF get_all_champions if you prefer a dictionary. Calling both will rescrape the entire website.

    Parameters:
    - verbose (bool): Choose whether to print the real time progress of the scraper

    Returns:
    - dict[str, Champion]: A dictionary with the champion name as the key and the Champion object as the value
    """

    champions: list[Champion] = get_all_champions(verbose)

    champion_dictionary: dict[str, Champion] = {}

    for champion in champions:
        champion_dictionary[champion.name] = champion

    return champion_dictionary
