import math
import random

import esper
import pygame

from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.ecs.components.c_input_command import CInputCommand

from src.ecs.components.tags.c_tag_enemy import CTagEnemy
from src.ecs.components.tags.c_tag_player import CTagPlayer
from src.ecs.components.tags.c_tag_bullet import CTagBullet


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
    world.add_component(sprite_entity, CSurface(size, color))
    world.add_component(sprite_entity, CTransform(pos))
    world.add_component(sprite_entity, CVelocity(vel))
    return sprite_entity


def create_enemy_square(world: esper.World, pos: pygame.Vector2, enemy_info: dict) -> int:
    enemy_sprite = pygame.image.load(enemy_info["image"]).convert_alpha()
    speed = random.uniform(enemy_info["velocity_min"], enemy_info["velocity_max"])
    angle = random.uniform(0, 2 * math.pi)
    vel = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
    enemy_entity = create_sprite(world, pygame.Vector2(pos), vel, enemy_sprite)
    world.add_component(enemy_entity, CTagEnemy())
    return enemy_entity


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
    size = pygame.Vector2(player_info["size"]["x"], player_info["size"]["y"])
    color = pygame.Color(player_info["color"]["r"], player_info["color"]["g"], player_info["color"]["b"])
    pos = pygame.Vector2(player_lvl_info["position"]["x"], player_lvl_info["position"]["y"])
    vel = pygame.Vector2(0,0)
    player_entity = create_square(world, size, color, pos, vel)
    world.add_component(player_entity, CTagPlayer())
    return player_entity


def create_bullet(world: esper.World, bullet_info: dict, player_pos: pygame.Vector2,
                  player_size: pygame.Vector2, target_pos: pygame.Vector2) -> None:
    size = pygame.Vector2(bullet_info["size"]["x"], bullet_info["size"]["y"])
    color = pygame.Color(bullet_info["color"]["r"], bullet_info["color"]["g"], bullet_info["color"]["b"])
    player_center = player_pos + player_size / 2
    direction = target_pos - player_center
    if direction.length_squared() == 0:
        return
    vel = direction.normalize() * bullet_info["velocity"]
    pos = player_center - size / 2
    bullet_entity = create_square(world, size, color, pos, vel)
    world.add_component(bullet_entity, CTagBullet())
