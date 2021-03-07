"""Same as test_functions.py, except it verifies that the parameters of each instance are being set correctly."""
from tests.piping.initial_conditions import *


# Utility functions
def test_grav_flow():
    flow_rate = utility_formulas.gravity_flow_rate(2, 1.67)
    assert flow_rate == 319.28008077388426


def test_static_press():
    press = utility_formulas.static_press(14)
    assert press == 6.068373888888889


# Gate Valve 1
def test_v1_input_press():
    assert valve1.press_in == 6.068373888888889


def test_v1_input_flow():
    assert valve1.flow_in == 319.28008077388426


def test_v1_press_drop():
    assert valve1.deltaP == 2.5484942494744516


def test_v1_output_flow():
    assert valve1.flow_out == 319.28008077388426


def test_v1_press_out():
    assert valve1.press_out == 3.5198796394144374


# Centrifugal Pump
def test_pump1_input_press():
    assert pump1.head_in == 8.119222584669064


def test_pump1_start_pump():
    assert pump1.speed == 1750
    assert pump1.flow == 50
    assert pump1.outlet_pressure == 16
    assert pump1.power == 0.11770474358069433


# Globe valve 1
def test_t1_input_press():
    assert throttle1.press_in == 16


def test_t1_input_flow():
    assert throttle1.flow_in == 50.0


def test_t1_press_drop():
    assert throttle1.deltaP == 5.668934240362812


def test_t1_output_flow():
    assert throttle1.flow_out == 50.0


def test_t1_press_out():
    assert throttle1.press_out == 10.331065759637188


# Gate Valve 2
def test_v2_input_press():
    assert valve2.press_in == 10.331065759637188


def test_v2_input_flow():
    assert valve2.flow_in == 50.0


def test_v2_press_drop():
    assert valve2.deltaP == 0.0625


def test_v2_output_flow():
    assert valve2.flow_out == 50.0


def test_v2_press_out():
    assert valve2.press_out == 10.268565759637188


# Gate Valve 3
def test_v3_input_press():
    assert valve3.press_in == 10.268565759637188


def test_v3_input_flow():
    assert valve3.flow_in == 50.0


def test_v3_press_drop():
    assert valve3.deltaP == 0.0625


def test_v3_output_flow():
    assert valve3.flow_out == 50.0


def test_v3_press_out():
    assert valve3.press_out == 10.206065759637188


# Gear Pump
def test_pump2_input_press():
    assert pump2.head_in == 23.542088964737797


def test_pump2_output():
    assert pump2.speed == 300
    assert pump2.flow == 28.8
    assert pump2.power == 0.10753003776038036


# Relief Valve 1
def test_relief1_input_press():
    assert relief1.press_in == 30


# Globe Valve 2
def test_t2_input_press():
    assert recirc1.press_in == 30


def test_t2_input_flow():
    assert recirc1.flow_in == 28.8


def test_2_press_drop():
    assert recirc1.deltaP == 1.8808163265306124


def test_t2_output_flow():
    assert recirc1.flow_out == 28.8


def test_t2_press_out():
    assert recirc1.press_out == 28.119183673469387


# Gate Valve 4
def test_v4_input_press():
    assert valve4.press_in == 28.119183673469387


def test_v4_input_flow():
    assert valve4.flow_in == 28.8


def test_v4_press_drop():
    assert valve4.deltaP == 0.020736000000000004


def test_v4_output_flow():
    assert valve4.flow_out == 28.800000000000004


def test_v4_press_out():
    assert valve4.press_out == 28.098447673469387
