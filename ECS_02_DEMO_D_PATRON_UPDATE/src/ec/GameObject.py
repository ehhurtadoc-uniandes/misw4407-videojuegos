from __future__ import annotations

from typing import TypeVar, cast

from src.ec.Component import Component

TCmp = TypeVar("TCmp", bound=Component)


class GameObject:
    def __init__(self) -> None:
        self._components: dict[type[Component], Component | None] = {}

    def add_component(self, cmp: TCmp) -> TCmp:
        cmp.game_object = self
        self._components[type(cmp)] = cast(Component, cmp)
        return cmp

    def remove_component(self, cmp_type: type[TCmp]) -> None:
        self._components[cmp_type] = None

    def get_component(self, cmp_type: type[TCmp]) -> TCmp | None:
        return cast(TCmp, self._components[cmp_type])

    def start(self) -> None:
        for cmp in self._components.values():
            if cmp is None:
                continue
            if not cmp.started:
                cmp.start()
                cmp.started = True

    def update(self, delta_time: float) -> None:
        for cmp in self._components.values():
            if cmp is None:
                continue
            cmp.update(delta_time)

    def draw(self) -> None:
        for cmp in self._components.values():
            if cmp is None:
                continue
            cmp.draw()

    def post_draw(self) -> None:
        for cmp in self._components.values():
            if cmp is None:
                continue
            cmp.post_draw()

    def post_loop(self) -> None:
        for cmp in self._components.values():
            if cmp is None:
                continue
            if cmp.destroyed:
                self._components.pop(type(cmp))
