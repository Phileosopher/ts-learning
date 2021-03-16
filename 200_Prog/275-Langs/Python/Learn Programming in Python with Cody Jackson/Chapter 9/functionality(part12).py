# Change tank level
def change_tank_level(tank, level):
    tank.level = level
    tank.static_tank_press = tank.level
    if tank == ffc.tank1:
        ffc.gate1.press_in = ffc.tank1.static_tank_press
    elif tank == ffc.tank2:
        ffc.gate2.press_in = ffc.tank2.static_tank_press
    else:
        return "Invalid tank number."
