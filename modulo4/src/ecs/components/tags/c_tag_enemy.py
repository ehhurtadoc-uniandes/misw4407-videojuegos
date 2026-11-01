from enum import Enum


class CTagEnemy:
    def __init__(self, enemy_type: "EnemyType") -> None:
        self.enemy_type = enemy_type


class EnemyType(Enum):
    BOUNCER = 0
    HUNTER = 1
