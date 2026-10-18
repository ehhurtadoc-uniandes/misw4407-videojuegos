import esper

from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.create.prefab_creator import create_enemy_square


def system_enemy_spawner(world: esper.World, enemies_cfg: dict, delta_time: float) -> None:
    components = world.get_component(CEnemySpawner)
    c_spw: CEnemySpawner
    for _, c_spw in components:
        c_spw.elapsed_time += delta_time
        for event in c_spw.spawn_events:
            if not event.triggered and c_spw.elapsed_time >= event.time:
                create_enemy_square(world, event.position, enemies_cfg[event.enemy_type])
                event.triggered = True
