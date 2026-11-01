import math
import random

import esper
import pygame

from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_enemy_hunter import CEnemyHunter
from src.ecs.components.c_player_state import CPlayerState
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_input_command import CInputCommand

from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_player import CTagPlayer
from src.ecs.components.tags.c_tag_bullet import CTagBullet
from src.ecs.components.tags.c_tag_explosion import CTagExplosion


def create_square(world: esper.World, size: pygame.Vector2, color: pygame.Color,
                  pos: pygame.Vector2, vel: pygame.Vector2) -> int:
    cuad_entity = world.create_entity()
    world.add_component(cuad_entity, CSurface(size, color))
    world.add_component(cuad_entity, CTransform(pos))
    world.add_component(cuad_entity, CVelocity(vel))
    return cuad_entity

def create_sprite(world: esper.World, pos: pygame.Vector2, vel: pygame.Vector2,
                  surface: pygame.Surface) -> int:
    sprite_entity = world.create_entity()
    world.add_component(sprite_entity, CSurface.from_surface(surface))
    world.add_component(sprite_entity, CTransform(pos))
    world.add_component(sprite_entity, CVelocity(vel))
    return sprite_entity


def create_enemy(world: esper.World, pos: pygame.Vector2, enemy_info: dict) -> int:
    if "velocity_chase" in enemy_info:
        return create_enemy_hunter(world, pos, enemy_info)
    return create_enemy_square(world, pos, enemy_info)


def create_enemy_square(world: esper.World, pos: pygame.Vector2, enemy_info: dict) -> int:
    enemy_sprite = pygame.image.load(enemy_info["image"]).convert_alpha()
    speed = random.uniform(enemy_info["velocity_min"], enemy_info["velocity_max"])
    angle = random.uniform(0, 2 * math.pi)
    vel = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
    enemy_entity = create_sprite(world, pygame.Vector2(pos), vel, enemy_sprite)
    world.add_component(enemy_entity, CTagEnemy())
    _add_animation(world, enemy_entity, enemy_info)
    return enemy_entity


def create_enemy_hunter(world: esper.World, pos: pygame.Vector2, hunter_info: dict) -> int:
    hunter_sprite = pygame.image.load(hunter_info["image"]).convert_alpha()
    hunter_entity = create_sprite(world, pygame.Vector2(pos), pygame.Vector2(0, 0), hunter_sprite)
    world.add_component(hunter_entity, CTagEnemy())
    world.add_component(hunter_entity, CEnemyHunter(pos, hunter_info))
    _add_animation(world, hunter_entity, hunter_info)
    return hunter_entity


def create_enemy_spawner(world: esper.World, level_cfg: dict) -> int:
    spawner_entity = world.create_entity()
    world.add_component(spawner_entity, CEnemySpawner(level_cfg))
    return spawner_entity

def create_input_player(world: esper.World) -> None:
    input_left = world.create_entity()
    input_right = world.create_entity()
    input_up = world.create_entity()
    input_down = world.create_entity()
    input_fire = world.create_entity()
    world.add_component(input_left, CInputCommand("PLAYER_LEFT", pygame.K_LEFT))
    world.add_component(input_right, CInputCommand("PLAYER_RIGHT", pygame.K_RIGHT))
    world.add_component(input_up, CInputCommand("PLAYER_UP", pygame.K_UP))
    world.add_component(input_down, CInputCommand("PLAYER_DOWN", pygame.K_DOWN))
    world.add_component(input_fire, CInputCommand("PLAYER_FIRE", pygame.BUTTON_LEFT))


def create_player_square(world: esper.World, player_info: dict, player_lvl_info: dict) -> int:
    player_sprite = pygame.image.load(player_info["image"]).convert_alpha()
    size = _get_frame_size(player_sprite, player_info)
    pos = pygame.Vector2(player_lvl_info["position"]["x"] - (size.x / 2),
                         player_lvl_info["position"]["y"] - (size.y / 2))
    vel = pygame.Vector2(0, 0)
    player_entity = create_sprite(world, pos, vel, player_sprite)
    world.add_component(player_entity, CTagPlayer())
    world.add_component(player_entity, CPlayerState())
    _add_animation(world, player_entity, player_info)
    return player_entity


def create_bullet(world: esper.World, bullet_info: dict, player_pos: pygame.Vector2,
                  player_size: pygame.Vector2, target_pos: pygame.Vector2) -> None:
    bullet_surface = pygame.image.load(bullet_info["image"]).convert_alpha()
    player_center = player_pos + player_size / 2
    direction = target_pos - player_center
    if direction.length_squared() == 0:
        return
    vel = direction.normalize() * bullet_info["velocity"]
    bullet_size = _get_frame_size(bullet_surface, bullet_info)
    pos = player_center - bullet_size / 2
    bullet_entity = create_sprite(world, pos, vel, bullet_surface)
    world.add_component(bullet_entity, CTagBullet())
    _add_animation(world, bullet_entity, bullet_info)


def create_explosion(world: esper.World, center: pygame.Vector2, explosion_info: dict) -> int:
    explosion_surface = pygame.image.load(explosion_info["image"]).convert_alpha()
    size = _get_frame_size(explosion_surface, explosion_info)
    pos = pygame.Vector2(center) - size / 2
    explosion_entity = create_sprite(world, pos, pygame.Vector2(0, 0), explosion_surface)
    world.add_component(explosion_entity, CTagExplosion())
    _add_animation(world, explosion_entity, explosion_info)
    return explosion_entity


def _get_frame_size(surface: pygame.Surface, info: dict) -> pygame.Vector2:
    size = pygame.Vector2(surface.get_size())
    if "animations" in info:
        size.x /= info["animations"]["number_frames"]
    return size


def _add_animation(world: esper.World, entity: int, info: dict) -> None:
    if "animations" not in info:
        return
    c_a = CAnimation(info["animations"])
    world.add_component(entity, c_a)
    c_s = world.component_for_entity(entity, CSurface)
    c_s.area.w = c_s.surf.get_width() / c_a.number_frames
    c_s.area.x = c_s.area.w * c_a.current_frame
