    else:  # Pout from valves 3 & 4 is equal
        ffc.gate6.press_in = ffc.gate3.press_out  # doesn't matter which Pout to use
    ffc.gate6.flow_in = ffc.gate3.flow_out + ffc.gate4.flow_out  # combined flow from valves 3 & 4
	if ffc.gate1.position == 0 and (ffc.gate2.position == 0 or ffc.gate4.position == 0): # no input flow
        ffc.gate3.press_in = ffc.gate3.flow_in = ffc.gate3.press_out = ffc.gate3.flow_out = 0.0  # Ensure null values
    if ffc.gate2.position == 0:  # valve 3 provides flow to valve 4
        ffc.gate4.press_in = ffc.gate3.press_out
        ffc.gate4.flow_in = ffc.gate6.flow_in = ffc.gate3.flow_out
    if ffc.gate1.position == 0:  # valve 4 provides flow to valve 3
        ffc.gate5.press_in = ffc.gate3.press_out
        ffc.gate5.flow_in = ffc.gate6.flow_in = ffc.gate3.flow_out
