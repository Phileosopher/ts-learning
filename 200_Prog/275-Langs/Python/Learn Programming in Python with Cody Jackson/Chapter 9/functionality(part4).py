# Gate valve 3
def gate3_open():
    ffc.gate3.open()
    if ffc.gate1.position == 100 and ffc.gate2.position == 100 and ffc.gate4.position == 100:  # dual input
        if ffc.gate3.press_out > ffc.gate4.press_out:  # pressure from tank 1 > tank 2
            ffc.gate6.press_in = ffc.gate3.press_out
            ffc.gate4.press_in = ffc.gate3.press_out
        elif ffc.gate3.press_out < ffc.gate4.press_out:  # pressure from tank 1 < tank 2
            ffc.gate3.press_in = ffc.gate4.press_out
            ffc.gate6.press_in = ffc.gate4.press_out
