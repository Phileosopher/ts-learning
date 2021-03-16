#!/usr/bin/env python3

"""Provides standard starting conditions for all devices in the system.

Assumes valves in series, with the first supplied by a tank 10 feet above the valve with a pipe length of 6 feet.
Water level is 4 feet above tank bottom; total water head = 14 feet.
"""
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from Utilities import utility_formulas

from PipingSystems.pump.pump import CentrifPump, PositiveDisplacement
from PipingSystems.valve.valve import Gate, Globe, Relief

# Gate Valve 1
valve1 = Gate("Valve 1", position=100, flow_coeff=200, sys_flow_in=utility_formulas.gravity_flow_rate(2, 1.67),
              press_in=utility_formulas.static_press(14))
valve1.flow_out = valve1.flow_in
valve1.press_drop(valve1.flow_out)
valve1.get_press_out(valve1.press_in)

# Centrif Pump
pump1 = CentrifPump("Pump 1", pump_head_in=utility_formulas.press_to_head(valve1.press_out))
pump1.start_pump(1750, 50, 16)

# Globe valve 1
throttle1 = Globe("Throttle 1", position=100, flow_coeff=21, press_in=pump1.outlet_pressure,
                  sys_flow_in=pump1.flow)
throttle1.flow_out = throttle1.flow_in
throttle1.press_drop(throttle1.flow_out)
throttle1.valve_flow_out(throttle1.Cv, throttle1.deltaP)
throttle1.get_press_out(throttle1.press_in)

# Gate Valve 2
valve2 = Gate("Valve 2", position=100, flow_coeff=200, press_in=throttle1.press_out, sys_flow_in=throttle1.flow_out)
valve2.flow_out = valve2.flow_in
valve2.press_drop(valve2.flow_out)
valve2.valve_flow_out(valve2.Cv, valve2.deltaP)
valve2.get_press_out(valve2.press_in)

# Gate Valve 3
valve3 = Gate("Valve 3", position=100, flow_coeff=200, press_in=valve2.press_out, sys_flow_in=valve2.flow_out)
valve3.flow_out = valve3.flow_in
valve3.press_drop(valve3.flow_out)
valve3.valve_flow_out(valve3.Cv, valve3.deltaP)
valve3.get_press_out(valve3.press_in)

# Gear Pump
pump2 = PositiveDisplacement("Gear Pump", displacement=0.096, press_out=30,
                             pump_head_in=utility_formulas.press_to_head(valve3.press_out))
pump2.adjust_speed(300)

# Relief Valve 1
relief1 = Relief("Relief 1", open_press=60, close_press=55, press_in=pump2.outlet_pressure)

# Globe Valve 2
recirc1 = Globe("Throttle 2", position=100, flow_coeff=21, press_in=pump2.outlet_pressure,
                sys_flow_in=pump2.flow)
recirc1.flow_out = recirc1.flow_in
recirc1.press_drop(recirc1.flow_out)
recirc1.valve_flow_out(recirc1.Cv, recirc1.deltaP)
recirc1.get_press_out(recirc1.press_in)

# Gate Valve 4
valve4 = Gate("Valve 4", position=100, flow_coeff=200, press_in=recirc1.press_out, sys_flow_in=recirc1.flow_out)
valve4.flow_out = valve4.flow_in
valve4.press_drop(valve4.flow_out)
valve4.valve_flow_out(valve4.Cv, valve4.deltaP)
valve4.get_press_out(valve4.press_in)

if __name__ == "__main__":
    print(valve1.flow_out)
    print(valve1.deltaP)
    print(valve1.press_in)
    print(valve1.press_out)