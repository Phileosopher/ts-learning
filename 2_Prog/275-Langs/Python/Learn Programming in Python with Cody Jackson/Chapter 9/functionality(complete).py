#!/usr/bin/env python3
"""
FuelFarm_functionality.py

Purpose: Ensure valve/pump changes are passed to the rest of the system.

Author: Cody Jackson

Date: 6/18/18
#################################
Version 0.2
    Added path extension for utility formulas
Version 0.1
    Initial build
"""
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from Utilities import utility_formulas
import Models.FuelFarm.components as ffc

# TODO: log valve/pump changes


# Gate valve 1
def gate1_open():
    ffc.gate1.open()
    if ffc.tank2.static_tank_press > ffc.tank1.static_tank_press:
        ffc.gate1.flow_in = ffc.gate1.flow_out = 0.0
        ffc.gate3.press_in = ffc.gate4.press_out
        ffc.gate3.flow_in = 0.0  # No flow because of check valves after valves 1 & 2
    else:
        ffc.gate3.press_in = ffc.gate1.press_out
        ffc.gate3.flow_in = ffc.gate1.flow_out
        ffc.gate5.press_in = ffc.gate1.press_out
        ffc.gate5.flow_in = ffc.gate1.flow_out

# TODO: ensure that one tank on service allows flow


def gate1_close():
    ffc.gate1.close()
    ffc.gate3.press_in = ffc.gate4.press_out
    ffc.gate3.flow_in = ffc.gate4.flow_out
    ffc.gate5.press_in = ffc.gate3.press_out
    ffc.gate5.flow_in = ffc.gate3.flow_out


# Gate valve 2
def gate2_open():
    ffc.gate2.open()
    if ffc.tank2.static_tank_press < ffc.tank1.static_tank_press:
        ffc.gate2.flow_in = ffc.gate2.flow_out = 0.0
        ffc.gate4.press_in = ffc.gate3.press_out
        ffc.gate4.flow_in = 0.0  # No flow because of check valves after valves 1 & 2
    else:
        ffc.gate4.press_in = ffc.gate2.press_out
        ffc.gate4.flow_in = ffc.gate2.flow_out
        ffc.gate7.press_in = ffc.gate2.press_out
        ffc.gate7.flow_in = ffc.gate2.flow_out


def gate2_close():
    ffc.gate2.close()
    ffc.gate4.press_in = ffc.gate4.press_out
    ffc.gate4.flow_in = ffc.gate4.flow_out
    ffc.gate7.press_in = ffc.gate4.press_out
    ffc.gate7.flow_in = ffc.gate4.flow_out


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


def gate3_close():
    ffc.gate3.close()
    ffc.gate6.press_in = ffc.gate4.press_out
    ffc.gate6.flow_in = ffc.gate4.flow_out
    if ffc.gate2.position == 0:
        ffc.gate4.press_in = 0.0
        ffc.gate4.flow_in = 0.0


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


# Gate valve 5
def gate5_open():
    ffc.gate5.open()
    ffc.pump1.head_in = utility_formulas.press_to_head(ffc.gate5.press_out)


def gate5_close():
    ffc.gate5.close()
    ffc.pump1.head_in = 0.0


# Gate valve 6
def gate6_open():
    ffc.gate6.open()
    ffc.pump2.head_in = utility_formulas.press_to_head(ffc.gate6.press_out)


def gate6_close():
    ffc.gate6.close()
    ffc.pump2.head_in = 0.0


# Gate valve 7
def gate7_open():
    ffc.gate7.open()
    ffc.pump3.head_in = utility_formulas.press_to_head(ffc.gate7.press_out)


def gate7_close():
    ffc.gate7.close()
    ffc.pump3.head_in = 0.0

# TODO: Account for flow in/out of tanks


# Gate valve 8
def gate8_open():
    ffc.gate8.open()


def gate8_close():
    ffc.gate8.close()


# Gate valve 9
def gate9_open():
    ffc.gate9.open()


def gate9_close():
    ffc.gate9.close()


# Gate valve 10
def gate10_open():
    ffc.gate10.open()


def gate10_close():
    ffc.gate10.close()


# Change tank level
def change_tank_level(tank, level):
    tank.level = level
    tank.static_tank_press = tank.level
    if tank == ffc.tank1:
        ffc.gate1.press_in = ffc.tank1.static_tank_press
    elif tank == ffc.tank2:
        ffc.gate2.press_in = ffc.tank2.static_tank_press
    else:
        return "Invalid tank number."


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


# Pump 3
def pump3_on():
    ffc.pump3.adjust_speed(1480)
    ffc.pump3.outlet_pressure = ffc.gate8.press_in = ffc.gate10.press_in = 50
    ffc.gate8.flow_in = ffc.gate10.flow_in = ffc.pump3.flow + ffc.pump2.flow


def pump3_off():
    ffc.pump3.adjust_speed(0)
    ffc.pump3.outlet_pressure = 0
