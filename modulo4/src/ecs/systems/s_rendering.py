import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_text import CTagText


def system_rendering(world: esper.World, screen: pygame.Surface) -> None:
    components = world.get_components(CTransform, CSurface)
    c_t: CTransform
    c_s: CSurface
    for entity, (c_t, c_s) in components:
        if world.has_component(entity, CTagText):
            continue
        screen.blit(c_s.surf, c_t.pos, area= c_s.area)
