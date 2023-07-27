from json import JSONDecoder
from ability import Ability, AbilityEncoder, AbilityDecoder

class Champion:
    def __init__(self, name: str, abilities: list[Ability]):
        self.name = name
        self.abilities = abilities

    def __str__(self) -> str:
        return "{}:\n{}".format(self.name, "\n".join(["\t" + str(ability) for ability in self.abilities]))
    
    def __repr__(self) -> str:
        return "{}:\n{}".format(self.name, "\n".join(["\t" + str(ability) for ability in self.abilities]))

class ChampionEncoder(AbilityEncoder):
    def default(self, obj):
        if isinstance(obj, Champion):
            return {
                "name": obj.name,
                "abilities": obj.abilities
            }
        
        return super().default(obj)
    
class ChampionDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
            kwargs["object_hook"] = self.object_hook
            super().__init__(**kwargs)

            self.ability_decoder = AbilityDecoder()

    def object_hook(self, dct) -> Champion | Ability | dict:
        if "abilities" in dct:
            return Champion(
                dct["name"],
                dct["abilities"]
            )
        
        else:
            return self.ability_decoder.object_hook(dct)
