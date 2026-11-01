import esper
import pygame

from src.create.prefab_creator import create_explosion
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_bullet import CTagBullet


def system_collision_enemy_bullet(world: esper.World, explosion_info: dict) -> None:
    enemies = world.get_components(CTransform, CSurface, CTagEnemy)
    bullets = world.get_components(CTransform, CSurface, CTagBullet)
    c_t: CTransform
    c_s: CSurface
    for bullet_entity, (b_t, b_s, _) in bullets:
        bullet_rect = CSurface.get_area_relative(b_s.area, b_t.pos)
        for enemy_entity, (c_t, c_s, _) in enemies:
            if not world.entity_exists(enemy_entity):
                continue
            enemy_rect = CSurface.get_area_relative(c_s.area, c_t.pos)
            if enemy_rect.colliderect(bullet_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(bullet_entity)
                create_explosion(world, pygame.Vector2(enemy_rect.center), explosion_info)
                break
