import pygame


class SpawnEvent:
    def __init__(self, time: float, enemy_type: str, position: pygame.Vector2) -> None:
        self.time = time
        self.enemy_type = enemy_type
        self.position = position
        self.triggered = False


class CEnemySpawner:
    def __init__(self, level_cfg: dict) -> None:
        self.elapsed_time = 0.0
        self.spawn_events = [
            SpawnEvent(event["time"],
                       event["enemy_type"],
                       pygame.Vector2(event["position"]["x"], event["position"]["y"]))
            for event in level_cfg.get("enemy_spawn_events", [])
        ]
