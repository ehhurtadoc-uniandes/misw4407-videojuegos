from __future__ import annotations


class Component:
    def __init__(self):
        from src.ec.GameObject import GameObject

        self.game_object: GameObject
        self.started: bool = False
        self.destroyed: bool = False

    def start(self):
        pass

    def update(self, _delta_time: float):
        pass

    def draw(self):
        pass

    def post_draw(self):
        pass

    def destroy(self):
        self.destroyed = True
