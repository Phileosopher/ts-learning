"""Same as test_parameters.py, except it checks values after throttle valve 1 is turned."""
from .initial_conditions import *


# Turn Globe Valve 1
def test_throttle1_50_percent():
    throttle1.turn_handle(50)
    assert throttle1.press_in == 16.0
    assert throttle1.flow_in == 50.0
    assert throttle1.position == 50
    assert throttle1.deltaP == 1.417233560090703
    assert throttle1.flow_out == 25.0
    assert throttle1.press_out == 14.582766439909298


def test_valve2():
    valve2.flow_in = throttle1.flow_out
    valve2.flow_out = valve2.flow_in
    valve2.press_in = throttle1.press_out
    valve2.press_drop(valve2.flow_out)
    valve2.get_press_out(valve2.press_in)
    assert valve2.press_in == 14.582766439909298
    assert valve2.flow_in == 25.0
    assert valve2.deltaP == 0.015625
    assert valve2.press_out == 14.567141439909298
    assert valve2.flow_out == 25.0


def test_valve3():
    valve3.flow_in = valve2.flow_out
    valve3.flow_out = valve3.flow_in
    valve3.press_in = valve2.press_out
    valve3.press_drop(valve3.flow_out)
    valve3.get_press_out(valve3.press_in)
    assert valve3.press_in == 14.567141439909298
    assert valve3.flow_in == 25.0
    assert valve3.deltaP == 0.015625
    assert valve3.press_out == 14.551516439909298
    assert valve3.flow_out == 25.0


def test_gear_pump():
    pump1.head_in = utility_formulas.press_to_head(valve3.press_out)
    assert pump1.head_in == 33.5656366192537


# Change Pump 1 Speed
def test_centrif_speed():
    pump1.adjust_speed(3000)
    assert pump1.flow == 85.71428571428571
    assert pump1.outlet_pressure == 47.0204081632653
    assert pump1.power == 1.21091176015825


def test_throttle_open():
    throttle1.open()  # Reset throttle to fully open
    throttle1.flow_in = pump1.flow
    throttle1.flow_out = throttle1.flow_in
    throttle1.press_in = pump1.outlet_pressure
    throttle1.press_out = throttle1.press_in
    throttle1.press_drop(throttle1.flow_out)
    throttle1.get_press_out(throttle1.press_in)
    assert throttle1.position == 100
    assert throttle1.flow_in == 85.71428571428571
    assert throttle1.flow_out == 85.71428571428571
    assert throttle1.press_in == 47.0204081632653
    assert throttle1.deltaP == 16.65972511453561
    assert throttle1.press_out == 30.36068304872969


def test_throttle_half_open():
    throttle1.turn_handle(50)
    assert throttle1.press_in == 47.0204081632653
    assert throttle1.flow_in == 85.71428571428571
    assert throttle1.position == 50
    assert throttle1.deltaP == 4.164931278633903
    assert throttle1.flow_out == 42.857142857142854
    assert throttle1.press_out == 42.8554768846314
