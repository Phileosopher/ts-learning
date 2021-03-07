# Gate valve 2
def gate2_open():
    ffc.gate2.open()
    if ffc.tank2.static_tank_press < ffc.tank1.static_tank_press:
        ffc.gate2.flow_in = ffc.gate2.flow_out = 0.0
        ffc.gate4.press_in = ffc.gate3.press_out
        ffc.gate4.flow_in = 0.0  # No flow because of check valves after valves 1 & 2
    else:
        ffc.gate4.press_in = ffc.gate2.press_out
        ffc.gate4.flow_in = ffc.gate2.flow_out
        ffc.gate7.press_in = ffc.gate2.press_out
        ffc.gate7.flow_in = ffc.gate2.flow_out

def gate2_close():
    ffc.gate2.close()
    ffc.gate4.press_in = ffc.gate4.press_out
    ffc.gate4.flow_in = ffc.gate4.flow_out
    ffc.gate7.press_in = ffc.gate4.press_out
    ffc.gate7.flow_in = ffc.gate4.flow_out
