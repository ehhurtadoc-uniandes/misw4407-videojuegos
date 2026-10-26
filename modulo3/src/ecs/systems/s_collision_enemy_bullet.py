import esper

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_bullet import CTagBullet


def system_collision_enemy_bullet(world: esper.World) -> None:
    enemies = world.get_components(CTransform, CSurface, CTagEnemy)
    bullets = world.get_components(CTransform, CSurface, CTagBullet)
    c_t: CTransform
    c_s: CSurface
    for bullet_entity, (b_t, b_s, _) in bullets:
        bullet_rect =  b_s.area.copy()
        bullet_rect.topleft = b_t.pos
        for enemy_entity, (c_t, c_s, _) in enemies:
            if not world.entity_exists(enemy_entity):
                continue
            enemy_rect = c_s.area.copy()
            enemy_rect.topleft = c_t.pos
            if enemy_rect.colliderect(bullet_rect):
                world.delete_entity(enemy_entity)
                world.delete_entity(bullet_entity)
                break
