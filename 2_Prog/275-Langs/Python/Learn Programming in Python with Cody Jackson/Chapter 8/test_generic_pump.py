import pytest
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from PipingSystems.pump.pump import Pump


class TestPumpSpeed:
    def test_speed_control_expected(self):
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        p.speed = 750
        assert p.speed == 750

    def test_speed_control_zero(self):
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        p.speed = 0
        assert p.speed == 0

    def test_speed_control_neg(self):
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        with pytest.raises(ValueError) as excinfo:
            p.speed = -10
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Speed must be 0 or greater."

    def test_speed_control_non_int(self):
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        with pytest.raises(TypeError):
            p.speed = "a"


class TestPumpReadSpeed:
    def test_cls_read_speed_expected(self):
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        assert p.speed == 300


class TestPumpReadPress:
    def test_cls_read_press(self):
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        assert p.outlet_pressure == 45.0


class TestPumpReadFlow:
    def test_cls_read_flow(self):
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        assert p.flow == 100.0


class TestPumpReadPower:
    def test_cls_read_power(self):
        # self.wattage = self.pump_power(self.flow_rate, self.diff_press(self.head, self.outlet_pressure))
        p = Pump(name="", flow_rate_out=100, pump_head_in=12, press_out=45, pump_speed=300)
        assert p.power == 0.6224710060377437
