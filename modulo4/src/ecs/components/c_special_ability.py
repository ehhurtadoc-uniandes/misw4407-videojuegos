from enum import Enum


class CSpecialAbility:
    def __init__(self, special_info: dict) -> None:
        self.duration = special_info["duration"]
        self.cooldown = special_info["cooldown"]
        self.radius = special_info["radius"]
        self.timer = 0.0
        self.state = AbilityState.READY


class AbilityState(Enum):
    READY = 0
    ACTIVE = 1
    COOLDOWN = 2
