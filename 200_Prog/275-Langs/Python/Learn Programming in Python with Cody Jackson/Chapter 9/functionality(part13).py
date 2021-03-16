# Pump 1
def pump1_on():
    ffc.pump1.adjust_speed(1480)
    ffc.pump1.outlet_pressure = ffc.gate9.press_in = 50
    ffc.gate9.flow_in = ffc.pump1.flow

def pump1_off():
    ffc.pump1.adjust_speed(0)
    ffc.pump1.outlet_pressure = 0

# Pump 2
def pump2_on():
    ffc.pump2.adjust_speed(1480)
    ffc.pump2.outlet_pressure = ffc.gate8.press_in  = ffc.gate10.press_in = 50
    ffc.gate8.flow_in = ffc.gate10.flow_in = ffc.pump2.flow + ffc.pump3.flow

def pump2_off():
    ffc.pump2.adjust_speed(0)
    ffc.pump2.outlet_pressure = 0
