import esper
import pygame

from src.ecs.components.c_pulse import CPulse
from src.ecs.components.c_surface import CSurface


def system_pulse(world: esper.World, delta_time: float) -> None:
    components = world.get_components(CSurface, CPulse)
    c_s: CSurface
    c_p: CPulse
    for _, (c_s, c_p) in components:
        c_p.elapsed_time += delta_time
        progress = min(c_p.elapsed_time / c_p.expand_time, 1.0)
        current_radius = int(c_p.radius * progress)
        c_s.surf.fill((0, 0, 0, 0))
        if current_radius > 0:
            pygame.draw.circle(c_s.surf, c_p.color, c_s.surf.get_rect().center,
                               current_radius, c_p.thickness)
