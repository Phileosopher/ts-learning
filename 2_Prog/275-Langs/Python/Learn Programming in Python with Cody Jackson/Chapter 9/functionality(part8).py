    if ffc.gate1.position == 0:  # valve 4 provides flow to valve 3
        ffc.gate3.press_in = ffc.gate4.press_out
        ffc.gate3.flow_in = ffc.gate6.flow_in = ffc.gate4.flow_out
    if ffc.gate2.position == 0:  # valve 3 provides flow to valve 4
        ffc.gate7.press_in = ffc.gate4.press_out
        ffc.gate7.flow_in = ffc.gate6.flow_in = ffc.gate4.flow_out

def gate4_close():
    ffc.gate4.close()
    ffc.gate6.press_in = ffc.gate3.press_out
    ffc.gate6.flow_in = ffc.gate3.flow_out
    if ffc.gate1.position == 0:
        ffc.gate3.press_in = 0.0
        ffc.gate3.flow_in = 0.0
