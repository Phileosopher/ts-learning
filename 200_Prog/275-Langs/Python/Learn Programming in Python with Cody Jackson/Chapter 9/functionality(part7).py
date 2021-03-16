# Gate valve 4
def gate4_open():
    ffc.gate4.open()
    if ffc.gate2.position == 100 and ffc.gate1.position == 100 and ffc.gate3.position == 100:  # dual input
        if ffc.gate3.press_out > ffc.gate4.press_out:  # pressure from tank 1 > tank 2
            ffc.gate6.press_in = ffc.gate3.press_out
            ffc.gate4.press_in = ffc.gate3.press_out
        elif ffc.gate3.press_out < ffc.gate4.press_out:  # pressure from tank 1 < tank 2
            ffc.gate6.press_in = ffc.gate4.press_out
            ffc.gate3.press_in = ffc.gate4.press_out
    else:  # Pout from valves 3 & 4 is equal
        ffc.gate6.press_in = ffc.gate4.press_out  # doesn't matter which Pout to use
    ffc.gate6.flow_in = ffc.gate4.flow_out + ffc.gate3.flow_out  # combined flow from valves 3 & 4
	if ffc.gate2.position == 0 and (ffc.gate1.position == 0 or ffc.gate3.position == 0):  # no input flow
        ffc.gate4.press_in = ffc.gate4.flow_in = ffc.gate4.press_out = ffc.gate4.flow_out = 0.0  # ensure null values
