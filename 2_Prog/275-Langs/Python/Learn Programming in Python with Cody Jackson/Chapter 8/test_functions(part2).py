pump2 = PositiveDisplacement("Gear Pump", displacement=0.096, press_out=30)
relief1 = Relief("Relief 1",  position=0, open_press=60, close_press=55)
recirc1 = Globe("Throttle 2", position=100, flow_coeff=21)
valve4 = Gate("Valve 4",  position=100, flow_coeff=200)

# Utility functions
def test_grav_flow():
    flow_rate = utility_formulas.gravity_flow_rate(2, 1.67)
    assert flow_rate == 319.28008077388426


def test_static_press():
    press = utility_formulas.static_press(14)
    assert press == 6.068373888888889
