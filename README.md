# LoL Wiki Scraper

This python module is a very barebones web scraper of the [League of Legends fandom wiki](https://leagueoflegends.fandom.com/wiki/League_of_Legends_Wiki) to pull every champion name, their ability name, and ability cooldown(s). I made this purely because I wanted an easy and automatic way to access the cooldowns of every champion for every patch. As a result, for now, it is very barebones and basic, but I may expand upon it later.

# How to use
- The [ability](./ability.py) module contains an Ability and AbilitySlot class to represent abilities
- The [champion](./champion.py) module contains a Champion class that has a name and a list of Ability objects
- The [scrape](./scrape.py) module contains several very useful functions that will scrape the LoL wiki to get a single champion or every champion, depending on what you want.
- The [demo](./demo.py) file has some examples showing how to use the program, primarily the scraper.
- The [utils](./utils.py) file has soe useful functions like exporting the data into json and csv (incomplete)