from enum import Enum

class AbilitySlot(Enum):
    PASSIVE = 0
    Q = 1
    W = 2
    E = 3
    R = 4
    OTHER = 5

    def __str__(self) -> str:
        return self.name.capitalize()

    @staticmethod
    def class_to_abilityslot(class_: str):
        if class_ == "skill_innate":
            return AbilitySlot.PASSIVE
        elif class_ == "skill_q":
            return AbilitySlot.Q
        elif class_ == "skill_w":
            return AbilitySlot.W
        elif class_ == "skill_e":
            return AbilitySlot.E
        elif class_ == "skill_r":
            return AbilitySlot.R
        else:
            return AbilitySlot.OTHER

class Ability:
    def __init__(self, name: str, slot: AbilitySlot, cooldowns: list[int] | str | None):
        self.name = name
        self.slot = slot
        self.cooldowns = cooldowns

    def __str__(self) -> str:
        return "{}: {} @ {}".format(str(self.slot), self.name, self.cooldowns)

    def __repr__(self) -> str:
        return "{}: {} @ {}".format(str(self.slot), self.name, self.cooldowns)
