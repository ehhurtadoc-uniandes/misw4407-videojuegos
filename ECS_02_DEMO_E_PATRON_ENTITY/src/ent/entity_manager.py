import pygame

from src.ent.entity import Entity


class EntityManager:
    def __init__(self):
        self._entities: list[Entity] = []

    def add_entity(self, entity: Entity) -> None:
        if entity not in self._entities:
            entity.start()
            self._entities.append(entity)

    def update(self, delta_time: float) -> None:
        for entity in self._entities:
            entity.update(delta_time)

    def draw(self, screen: pygame.Surface) -> None:
        for entity in self._entities:
            entity.draw(screen)

    def clear_all(self):
        self._entities.clear()
