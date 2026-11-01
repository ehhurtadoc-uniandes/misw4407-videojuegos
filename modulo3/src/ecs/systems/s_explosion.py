import esper

from src.ecs.components.c_animation import CAnimation
from src.ecs.components.tags.c_tag_explosion import CTagExplosion


def system_explosion(world: esper.World) -> None:
    components = world.get_components(CAnimation, CTagExplosion)
    c_a: CAnimation
    for explosion_entity, (c_a, _) in components:
        if c_a.completed_loops > 0:
            world.delete_entity(explosion_entity)
