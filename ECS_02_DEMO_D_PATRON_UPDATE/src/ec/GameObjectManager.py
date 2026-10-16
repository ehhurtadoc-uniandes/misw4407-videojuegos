from src.ec.GameObject import GameObject


class GameObjectManager:
    def __init__(self) -> None:
        self._game_objects: list[GameObject] = []
        self._game_objects_to_add: list[GameObject] = []
        self._game_objects_to_kill: list[GameObject] = []

    def create_game_object(self) -> GameObject:
        go = GameObject()
        self._game_objects_to_add.append(go)
        return go

    def pre_loop(self) -> None:
        for go in self._game_objects:
            go.start()

    def update(self, delta_time: float) -> None:
        for go in self._game_objects:
            go.update(delta_time)

    def draw(self) -> None:
        for go in self._game_objects:
            go.draw()

    def post_draw(self) -> None:
        for go in self._game_objects:
            go.post_draw()

    def post_loop(self) -> None:
        for go in self._game_objects_to_kill:
            self._game_objects.remove(go)
        for go in self._game_objects_to_add:
            self._game_objects.append(go)

        self._game_objects_to_kill.clear()
        self._game_objects_to_add.clear()

    def clear_all(self):
        self._game_objects.clear()
        self._game_objects_to_kill.clear()
        self._game_objects_to_add.clear()
