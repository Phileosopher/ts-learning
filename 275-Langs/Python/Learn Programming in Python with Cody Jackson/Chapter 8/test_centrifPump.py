import pytest
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])

from PipingSystems.pump.pump import CentrifPump


class TestPumpSpeed():
    def test_get_speed_expected(self):
        p = CentrifPump(pump_speed=450)
        assert p.get_speed_str() == "The pump is running at 450 rpm."

    def test_get_speed_zero(self):
        p = CentrifPump(pump_speed=0)
        assert p.get_speed_str() == "The pump is stopped."


class TestFlowrate:
    def test_get_flowrate(self):
        p = CentrifPump(flow_rate_out=100.0)
        assert p.get_flow_str() == "The pump output flow rate is 100.0 gpm."


class TestPressure:
    def test_get_pressure(self):
        p = CentrifPump(press_out=55.5)
        assert p.get_press_str() == "The pump pressure is 55.50 psi."


class TestPower:
    def test_get_power(self):
        p = CentrifPump("", 100, 12, 45, 300)
        assert p.get_power_str() == "The power usage for the pump is 0.62 kW."


class TestChangeSpeed:
    def test_adjust_speed_expected(self):
        p = CentrifPump("", flow_rate_out=75, pump_head_in=3, press_out=7.3, pump_speed=1750)
        p.adjust_speed(500)
        assert p.get_speed_str() == "The pump is running at 500 rpm."
        assert p.get_flow_str() == "The pump output flow rate is 21.428571428571427 gpm."
        assert p.get_press_str() == "The pump pressure is 0.60 psi."
        assert p.get_power_str() == "The power usage for the pump is 0.01 kW."

    def test_adjust_speed_neg(self):
        p = CentrifPump("", 100, 12, 45, 300)
        with pytest.raises(ValueError) as excinfo:
            p.adjust_speed(-100)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Speed must be 0 or greater."

    def test_adjust_speed_zero(self):
        p = CentrifPump("", 100, 12, 45, 300)
        p.adjust_speed(0)
        assert p.get_speed_str() == "The pump is stopped."
        assert p.get_flow_str() == "The pump output flow rate is 0.0 gpm."
        assert p.get_press_str() == "The pump pressure is 0.00 psi."
        assert p.get_power_str() == "The power usage for the pump is 0.00 kW."

    def test_adjust_speed_non_int(self):
        p = CentrifPump("", 100, 12, 45, 300)
        with pytest.raises(TypeError):
            p.adjust_speed("a")


class TestPumpLaws:
    def test_pump_laws_expected(self):
        p = CentrifPump("", flow_rate_out=75, pump_head_in=3, press_out=7.3, pump_speed=1750)
        p.adjust_speed(500)
        assert p.flow == 21.428571428571427
        assert p.outlet_pressure == 0.5959183673469387
        assert p.power == 0.006569936061502869

    def test_pump_laws_zero(self):
        p = CentrifPump("", 100, 12, 45, 300)
        p.adjust_speed(0)
        assert p.flow == 0.0
        assert p.outlet_pressure == 0.0
        assert p.power == 0.0

    def test_pump_laws_neg(self):
        p = CentrifPump("", 100, 12, 45, 300)
        with pytest.raises(ValueError) as excinfo:
            p.speed = -120
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Speed must be 0 or greater."

    def test_pump_laws_non_int(self):
        p = CentrifPump("", 100, 12, 45, 300)
        with pytest.raises(TypeError) as excinfo:
            p.speed = "a"
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Numeric values only."
