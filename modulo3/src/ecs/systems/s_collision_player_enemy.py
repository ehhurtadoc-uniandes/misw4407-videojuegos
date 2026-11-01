import esper
import pygame

from src.create.prefab_creator import create_explosion
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_enemy import CTagEnemy


def system_collision_player_enemy(world: esper.World, player_entity: int, player_spawn: pygame.Vector2,
                                  explosion_info: dict) -> None:
    enemies = world.get_components(CTransform, CSurface, CTagEnemy)
    pl_t = world.component_for_entity(player_entity, CTransform)
    pl_s = world.component_for_entity(player_entity, CSurface)

    player_rect = CSurface.get_area_relative(pl_s.area, pl_t.pos)

    c_t: CTransform
    c_s: CSurface
    for enemy_entity, (c_t, c_s, _) in enemies:
        enemy_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
        if enemy_rect.colliderect(player_rect):
            world.delete_entity(enemy_entity)
            create_explosion(world, pygame.Vector2(enemy_rect.center), explosion_info)
            pl_t.pos.xy = player_spawn - pygame.Vector2(pl_s.area.size) / 2
