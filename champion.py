from ability import Ability

class Champion:
    def __init__(self, name: str, abilities: list[Ability]):
        self.name = name
        self.abilities = abilities

    def __str__(self) -> str:
        return "{}:\n{}".format(self.name, "\n".join(["\t" + str(ability) for ability in self.abilities]))
    
    def __repr__(self) -> str:
        return "{}:\n{}".format(self.name, "\n".join(["\t" + str(ability) for ability in self.abilities]))
