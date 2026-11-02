import random

import esper

from src.ecs.components.c_screen_shake import CScreenShake


def system_screen_shake(world: esper.World, delta_time: float) -> None:
    c_ss: CScreenShake
    for _, c_ss in world.get_component(CScreenShake):
        if c_ss.timer > 0:
            c_ss.timer -= delta_time
            c_ss.offset.xy = (random.uniform(-c_ss.intensity, c_ss.intensity),
                              random.uniform(-c_ss.intensity, c_ss.intensity))
        else:
            c_ss.offset.xy = (0, 0)
