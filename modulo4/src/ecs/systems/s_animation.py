import esper
from src.ecs.components.c_animation import CAnimation
from src.ecs.components.c_surface import CSurface


def system_animation(world: esper.World, delta_time: float):
    components = world.get_components(CSurface, CAnimation)

    c_s: CSurface
    c_a: CAnimation
    for _, (c_s, c_a) in components:
        anim = c_a.animations_list[c_a.current_animation]
        c_a.current_animation_time -= delta_time
        if c_a.current_animation_time <= 0:
            c_a.current_animation_time = anim.framerate
            c_a.current_frame += 1
            if c_a.current_frame > anim.end:
                c_a.current_frame = anim.start
                c_a.completed_loops += 1

        rect_surf = c_s.surf.get_rect()
        c_s.area.w = rect_surf.w / c_a.number_frames
        c_s.area.x = c_s.area.w * c_a.current_frame


def set_animation(c_a: CAnimation, name: str) -> None:
    for index, anim in enumerate(c_a.animations_list):
        if anim.name == name:
            if c_a.current_animation == index:
                return
            c_a.current_animation = index
            c_a.current_animation_time = anim.framerate
            c_a.current_frame = anim.start
            c_a.completed_loops = 0
            return
