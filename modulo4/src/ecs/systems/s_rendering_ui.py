import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_ui import CTagUI


def system_rendering_ui(world: esper.World, screen: pygame.Surface) -> None:
    components = world.get_components(CTransform, CSurface, CTagUI)
    c_t: CTransform
    c_s: CSurface
    for _, (c_t, c_s, _) in components:
        screen.blit(c_s.surf, c_t.pos, area= c_s.area)
