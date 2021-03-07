def static_press(height, density=WATER_DENSITY):
    """Calculate static pressure for any fluid"""
    press = density * GRAVITY * height / 144
    return press


def press_to_head(press, spec_grav=WATER_SPEC_GRAV):
    """Calculate fluid head from pressure."""
    head = (74.215 * press) / (spec_grav * GRAVITY)
    return head


def head_to_press(head, spec_grav=WATER_SPEC_GRAV):
    """Calculate pressure from fluid head."""
    press = (spec_grav * GRAVITY * head) / 74.215
    return press
