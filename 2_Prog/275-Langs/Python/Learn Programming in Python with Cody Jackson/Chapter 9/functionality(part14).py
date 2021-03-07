# Pump 3
def pump3_on():
    ffc.pump3.adjust_speed(1480)
    ffc.pump3.outlet_pressure = ffc.gate8.press_in = ffc.gate10.press_in = 50
    ffc.gate8.flow_in = ffc.gate10.flow_in = ffc.pump3.flow + ffc.pump2.flow

def pump3_off():
    ffc.pump3.adjust_speed(0)
    ffc.pump3.outlet_pressure = 0
