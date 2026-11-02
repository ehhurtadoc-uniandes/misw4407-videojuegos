import esper
import pygame

from src.ecs.components.c_screen_shake import CScreenShake
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_ui import CTagUI


def system_rendering(world: esper.World, screen: pygame.Surface) -> None:
    offset = pygame.Vector2(0, 0)
    for _, c_ss in world.get_component(CScreenShake):
        offset = c_ss.offset

    components = world.get_components(CTransform, CSurface)
    c_t: CTransform
    c_s: CSurface
    for entity, (c_t, c_s) in components:
        if world.has_component(entity, CTagUI):
            continue
        screen.blit(c_s.surf, c_t.pos + offset, area= c_s.area)
