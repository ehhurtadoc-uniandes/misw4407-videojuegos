from enum import Enum


class CPlayerState:
    def __init__(self, sound_move: str) -> None:
        self.state = PlayerState.IDLE
        self.sound_move = sound_move


class PlayerState(Enum):
    IDLE = 0
    MOVE = 1
