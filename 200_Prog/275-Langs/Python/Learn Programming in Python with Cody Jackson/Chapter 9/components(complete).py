#!/usr/bin/env python3
"""
FuelFarm.py

Purpose: Simulate an aviation fuel storage and transfer system.

Author: Cody Jackson

Date: 6/12/18
#################################
Version 0.2
    Added path extension for utility formulas
Version 0.1
    Initial build
"""
# TODO: rewrite to use a SQLite database
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from Utilities import utility_formulas

from PipingSystems.pump import pump
from PipingSystems.valve import valve
from PipingSystems.storage_tank import tank

# Constants
DENSITY = 1.629869
SPEC_GRAVITY = 0.840

# Storage tanks
# Assumes 36 ft tall tank w/ 1 million gallon capacity = 27778 gallons per foot
# Assumes 16 inch diam transfer piping
tank1 = tank.Tank("Tank 1", level=36.0, fluid_density=DENSITY, spec_gravity=SPEC_GRAVITY, outlet_diam=16,
                  outlet_slope=0.25)
tank1.static_tank_press = tank1.level
tank1.gravity_flow(tank1.pipe_diam, tank1.pipe_slope, tank1.pipe_coeff)

tank2 = tank.Tank("Tank 2", level=36.0, fluid_density=DENSITY, spec_gravity=SPEC_GRAVITY, outlet_diam=16,
                  outlet_slope=0.25)
tank2.static_tank_press = tank2.level
tank2.gravity_flow(tank2.pipe_diam, tank2.pipe_slope, tank2.pipe_coeff)

# Pump inlet manifold
# 16 inch to 4 inch connections
gate1 = valve.Gate("Gate valve 1", sys_flow_in=tank1.flow_out, press_in=tank1.static_tank_press)
gate1.calc_coeff(16)

gate2 = valve.Gate("Gate valve 2", sys_flow_in=tank2.flow_out, press_in=tank2.static_tank_press)
gate2.calc_coeff(16)

gate3 = valve.Gate("Gate valve 3")
gate3.calc_coeff(16)

gate4 = valve.Gate("Gate valve 4")
gate4.calc_coeff(16)

gate5 = valve.Gate("Gate valve 5")
gate5.calc_coeff(4)

gate6 = valve.Gate("Gate valve 6", sys_flow_in=gate3.flow_out + gate4.flow_out,
                   press_in=gate3.press_out + gate4.press_out)
gate6.calc_coeff(4)

gate7 = valve.Gate("Gate valve 7")
gate7.calc_coeff(4)

# Fuel pumps
# 1480 rpm
pump1 = pump.PositiveDisplacement("Pump 1",
                                  flow_rate_out=0.0,
                                  pump_head_in=utility_formulas.press_to_head(gate5.press_out),
                                  displacement=0.24)

pump2 = pump.PositiveDisplacement("Pump 2",
                                  flow_rate_out=0.0,
                                  pump_head_in=utility_formulas.press_to_head(gate6.press_out),
                                  displacement=0.24)

pump3 = pump.PositiveDisplacement("Pump 3",
                                  flow_rate_out=0.0,
                                  pump_head_in=utility_formulas.press_to_head(gate7.press_out),
                                  displacement=0.24)

# Pump outlet manifold
relief1 = valve.Relief("Relief 1", sys_flow_in=pump1.flow, flow_coeff=0.81)
relief2 = valve.Relief("Relief 2", sys_flow_in=pump2.flow, flow_coeff=0.81)
relief3 = valve.Relief("Relief 3", sys_flow_in=pump3.flow, flow_coeff=0.81)

throttle1 = valve.Globe("Flow Control 1", sys_flow_in=pump1.flow, press_in=pump1.outlet_pressure, flow_coeff=165)
throttle2 = valve.Globe("Flow Control 2", sys_flow_in=pump1.flow, press_in=pump1.outlet_pressure, flow_coeff=165)
throttle3 = valve.Globe("Flow Control 3", sys_flow_in=pump1.flow, press_in=pump1.outlet_pressure, flow_coeff=165)

gate8 = valve.Gate("Gate valve 8", sys_flow_in=throttle3.flow_out, press_in=throttle3.press_out)
gate8.calc_coeff(4)

gate9 = valve.Gate("Gate valve 9", sys_flow_in=throttle1.flow_out, press_in=throttle1.press_out)
gate9.calc_coeff(4)

gate10 = valve.Gate("Gate valve 10", sys_flow_in=throttle3.flow_out, press_in=throttle3.press_out)
gate10.calc_coeff(4)


if __name__ == "__main__":
    pass
