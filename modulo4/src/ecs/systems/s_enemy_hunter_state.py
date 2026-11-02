import esper
import pygame

from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_enemy_hunter import CEnemyHunter, HunterState
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.systems.s_animation import set_animation
from src.engine.service_locator import ServiceLocator


def system_enemy_hunter_state(world: esper.World, player_entity: int, delta_time: float) -> None:
    pl_t = world.component_for_entity(player_entity, CTransform)
    pl_s = world.component_for_entity(player_entity, CSurface)
    player_center = pl_t.pos + pygame.Vector2(pl_s.area.size) / 2

    components = world.get_components(CTransform, CVelocity, CSurface, CAnimation, CEnemyHunter)
    for _, (c_t, c_v, c_s, c_a, c_h) in components:
        hunter_center = c_t.pos + pygame.Vector2(c_s.area.size) / 2
        if c_h.state == HunterState.IDLE:
            _do_idle_state(c_v, c_a, c_h, hunter_center, player_center)
        elif c_h.state == HunterState.CHASE:
            _do_chase_state(c_t, c_v, c_a, c_h, hunter_center, player_center)
        elif c_h.state == HunterState.RETURN:
            _do_return_state(c_t, c_v, c_a, c_h, delta_time)


def _do_idle_state(c_v: CVelocity, c_a: CAnimation, c_h: CEnemyHunter,
                   hunter_center: pygame.Vector2, player_center: pygame.Vector2):
    set_animation(c_a, "IDLE")
    c_v.vel.xy = (0, 0)
    if hunter_center.distance_to(player_center) <= c_h.distance_start_chase:
        c_h.state = HunterState.CHASE
        ServiceLocator.sounds_service.play(c_h.sound_chase)


def _do_chase_state(c_t: CTransform, c_v: CVelocity, c_a: CAnimation, c_h: CEnemyHunter,
                    hunter_center: pygame.Vector2, player_center: pygame.Vector2):
    set_animation(c_a, "MOVE")
    direction = player_center - hunter_center
    if direction.length_squared() > 0:
        c_v.vel.xy = direction.normalize() * c_h.velocity_chase
    else:
        c_v.vel.xy = (0, 0)
    if c_t.pos.distance_to(c_h.origin) >= c_h.distance_start_return:
        c_h.state = HunterState.RETURN


def _do_return_state(c_t: CTransform, c_v: CVelocity, c_a: CAnimation, c_h: CEnemyHunter,
                     delta_time: float):
    set_animation(c_a, "MOVE")
    to_origin = c_h.origin - c_t.pos
    if to_origin.length() <= c_h.velocity_return * delta_time:
        c_t.pos.xy = c_h.origin
        c_v.vel.xy = (0, 0)
        c_h.state = HunterState.IDLE
    else:
        c_v.vel.xy = to_origin.normalize() * c_h.velocity_return
