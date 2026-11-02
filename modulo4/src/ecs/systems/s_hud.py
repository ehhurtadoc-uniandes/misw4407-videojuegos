import esper

from src.ecs.components.c_hud_bar import CHudBar
from src.ecs.components.c_hud_text import CHudText
from src.ecs.components.c_special_ability import CSpecialAbility, AbilityState
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform


def system_hud(world: esper.World) -> None:
    c_sa: CSpecialAbility
    for _, c_sa in world.get_component(CSpecialAbility):
        _update_bar(world, c_sa)
        _update_text(world, c_sa)


def _update_bar(world: esper.World, c_sa: CSpecialAbility) -> None:
    c_s: CSurface
    c_b: CHudBar
    for _, (c_s, c_b) in world.get_components(CSurface, CHudBar):
        if c_sa.state == AbilityState.READY:
            ratio, color = 1.0, c_b.color_ready
        elif c_sa.state == AbilityState.ACTIVE:
            ratio, color = c_sa.timer / c_sa.duration, c_b.color_active
        else:
            ratio, color = 1.0 - c_sa.timer / c_sa.cooldown, c_b.color_cooldown
        c_s.area.w = int(c_b.full_width * ratio)
        c_s.surf.fill(color)


def _update_text(world: esper.World, c_sa: CSpecialAbility) -> None:
    c_t: CTransform
    c_s: CSurface
    c_h: CHudText
    for _, (c_t, c_s, c_h) in world.get_components(CTransform, CSurface, CHudText):
        if c_sa.state == AbilityState.READY:
            text = c_h.text_ready
        elif c_sa.state == AbilityState.ACTIVE:
            text = c_h.text_active
        else:
            text = f"{c_sa.timer:.1f}"
        if text != c_h.current_text:
            c_h.current_text = text
            c_s.surf = c_h.font.render(text, False, c_h.color)
            c_s.area = c_s.surf.get_rect()
            c_t.pos.x = c_h.center_x - c_s.area.w / 2
