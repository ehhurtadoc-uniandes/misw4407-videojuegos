import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_enemy import CTagEnemy


def system_collision_player_enemy(world: esper.World, player_entity: int, player_spawn: pygame.Vector2) -> None:
    enemies = world.get_components(CTransform, CSurface, CTagEnemy)
    pl_t = world.component_for_entity(player_entity, CTransform)
    pl_s = world.component_for_entity(player_entity, CSurface)
    
    player_rect = pl_s.area.copy()
    player_rect.topleft = pl_t.pos
    
    c_t: CTransform
    c_s: CSurface
    for enemy_entity, (c_t, c_s, _) in enemies:
        enemy_rect = c_s.area.copy()
        enemy_rect.topleft = c_t.pos
        if enemy_rect.colliderect(player_rect):
            world.delete_entity(enemy_entity)
            pl_t.pos.xy = player_spawn
