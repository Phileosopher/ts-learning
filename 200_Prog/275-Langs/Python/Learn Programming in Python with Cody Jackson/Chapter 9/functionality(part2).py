# Gate valve 1
def gate1_open():
    ffc.gate1.open()
    if ffc.tank2.static_tank_press > ffc.tank1.static_tank_press:
        ffc.gate1.flow_in = ffc.gate1.flow_out = 0.0
        ffc.gate3.press_in = ffc.gate4.press_out
        ffc.gate3.flow_in = 0.0  # No flow because of check valves after valves 1 & 2
    else:
        ffc.gate3.press_in = ffc.gate1.press_out
        ffc.gate3.flow_in = ffc.gate1.flow_out
        ffc.gate5.press_in = ffc.gate1.press_out
        ffc.gate5.flow_in = ffc.gate1.flow_out

def gate1_close():
    ffc.gate1.close()
    ffc.gate3.press_in = ffc.gate4.press_out
    ffc.gate3.flow_in = ffc.gate4.flow_out
    ffc.gate5.press_in = ffc.gate3.press_out
    ffc.gate5.flow_in = ffc.gate3.flow_out
# TODO: ensure that one tank on service allows flow
