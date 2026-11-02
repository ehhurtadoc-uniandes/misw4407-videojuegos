import esper
import pygame

from src.create.prefab_creator import create_explosion
from src.ecs.components.c_screen_shake import CScreenShake
from src.ecs.components.c_special_ability import CSpecialAbility, AbilityState
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_shield import CTagShield


def system_special_ability(world: esper.World, player_entity: int, explosion_info: dict,
                           delta_time: float) -> None:
    pl_t = world.component_for_entity(player_entity, CTransform)
    pl_s = world.component_for_entity(player_entity, CSurface)
    player_center = pl_t.pos + pygame.Vector2(pl_s.area.size) / 2

    c_sa: CSpecialAbility
    for _, c_sa in world.get_component(CSpecialAbility):
        if c_sa.state == AbilityState.ACTIVE:
            _do_active_state(world, c_sa, player_center, explosion_info, delta_time)
        elif c_sa.state == AbilityState.COOLDOWN:
            _do_cooldown_state(c_sa, delta_time)


def _do_active_state(world: esper.World, c_sa: CSpecialAbility, player_center: pygame.Vector2,
                     explosion_info: dict, delta_time: float) -> None:
    for _, (c_t, c_s, _) in world.get_components(CTransform, CSurface, CTagShield):
        c_t.pos.xy = player_center - pygame.Vector2(c_s.area.size) / 2

    for enemy_entity, (c_t, c_s, _) in world.get_components(CTransform, CSurface, CTagEnemy):
        enemy_center = pygame.Vector2(CSurface.get_area_relative(c_s.area, c_t.pos).center)
        if world.entity_exists(enemy_entity) and enemy_center.distance_to(player_center) <= c_sa.radius:
            world.delete_entity(enemy_entity)
            create_explosion(world, enemy_center, explosion_info)
            _start_screen_shake(world)

    c_sa.timer -= delta_time
    if c_sa.timer <= 0:
        for shield_entity, _ in world.get_component(CTagShield):
            world.delete_entity(shield_entity)
        c_sa.state = AbilityState.COOLDOWN
        c_sa.timer = c_sa.cooldown


def _do_cooldown_state(c_sa: CSpecialAbility, delta_time: float) -> None:
    c_sa.timer -= delta_time
    if c_sa.timer <= 0:
        c_sa.timer = 0.0
        c_sa.state = AbilityState.READY


def _start_screen_shake(world: esper.World) -> None:
    c_ss: CScreenShake
    for _, c_ss in world.get_component(CScreenShake):
        c_ss.timer = c_ss.duration
