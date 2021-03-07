def gate3_close():
    ffc.gate3.close()
    ffc.gate6.press_in = ffc.gate4.press_out
    ffc.gate6.flow_in = ffc.gate4.flow_out
    if ffc.gate2.position == 0:
        ffc.gate4.press_in = 0.0
        ffc.gate4.flow_in = 0.0
