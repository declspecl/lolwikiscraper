# LoL Wiki Scraper

This python module is a basic web scraper of the [League of Legends fandom wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki) to pull every champion name, their ability name, and ability cooldown(s). I made this purely because I wanted an easy and automatic way to access the cooldowns of every champion for every patch. As a result, for now, it is very barebones, but I may expand upon it later.

# Dependencies
To install all the required dependencies, run
```py
pip install -r requirements.txt
```
on a cloned version of the repo. I am using Python 3.11.2 with pip 23.2.1

# How to use
- The [ability](./ability.py) module contains an Ability and AbilitySlot class to represent abilities
- The [champion](./champion.py) module contains a Champion class that has a name and a list of Ability objects
- The [scrape](./scrape.py) module contains several very useful functions that will scrape the LoL wiki to get a single champion or every champion, depending on what you want.
- The [demo](./demo.py) file has some examples showing how to use the program, primarily the scraper.
- The [utils](./utils.py) file has various useful functions that allow for exporting and important JSON data as well as

# Examples
I used a custom format using the [utils](./utils.py) module's `export_with_format` method to print some very nice looking pieces of data. Have a look:

## Markdown
### aatrox
#### cds
- Passive: 24 − 12 (based on level)
- Q: 14 / 12 / 10 / 8 / 6
- W: 20 / 18 / 16 / 14 / 12
- E: 9 / 8 / 7 / 6 / 5
- R: 120 / 100 / 80

### ahri
#### cds
- Passive: none
- Q: 7
- W: 9 / 8 / 7 / 6 / 5
- E: 14
- R: 130 / 105 / 80

## Plaintext
Rengar:
	Passive: Unseen Predator @ None
	Q: Savagery @ 6 / 5.5 / 5 / 4.5 / 4
	W: Battle Roar @ 16 / 14.5 / 13 / 11.5 / 10
	E: Bola Strike @ 10
	R: Thrill of the Hunt @ 110 / 100 / 90

Riven:
	Passive: Runic Blade @ None
	Q: Broken Wings @ 13
	W: Ki Burst @ 11 / 10 / 9 / 8 / 7
	E: Valor @ 10 / 9 / 8 / 7 / 6
	R: Blade of the Exile @ 120 / 90 / 60