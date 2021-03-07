"""Assumes valves in series, with the first supplied by a tank 10 feet above the valve with a pipe length of 6 feet.
Water level is 4 feet above tank bottom; total water head = 14 feet.
"""
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from Utilities import utility_formulas
from PipingSystems.pump.pump import CentrifPump, PositiveDisplacement
from PipingSystems.valve.valve import Gate, Globe, Relief

valve1 = Gate("Valve 1", position=100, flow_coeff=200, sys_flow_in=utility_formulas.gravity_flow_rate(2, 1.67),
              press_in=utility_formulas.static_press(14))
pump1 = CentrifPump("Pump 1")
throttle1 = Globe("Throttle 1", position=100, flow_coeff=21)
valve2 = Gate("Valve 2",  position=100, flow_coeff=200)
valve3 = Gate("Valve 3",  position=100, flow_coeff=200)
