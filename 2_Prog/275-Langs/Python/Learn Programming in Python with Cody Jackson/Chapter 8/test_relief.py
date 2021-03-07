import sys

sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from PipingSystems.valve.valve import Relief


class TestRelief():
    def test_read_position(self):
        r = Relief(name="Relief1")
        assert r.read_position() == "Relief1 is closed."

    def test_set_open_pressure(self):
        r = Relief(name="Relief1")
        r.set_open_pressure(25)
        assert r.setpoint_open == 25

    def test_set_blowdown(self):
        r = Relief(name="Relief1")
        r.set_close_press(10)
        assert r.setpoint_close == 10

    def test_valve_operation(self):
        r = Relief(name="Relief1", open_press=25, close_press=23)
        r.valve_operation(25)
        assert r.read_position() == "Relief1 is open."
        r.valve_operation(23)
        assert r.read_position() == "Relief1 is closed."
