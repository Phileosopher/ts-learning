import pytest
import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])
from PipingSystems.valve.valve import Valve


class TestValveCoeff:
    # self.Cv = 15 * math.pow(diameter, 2)
    def test_calc_coeff_expected(self):
        v = Valve()
        v.calc_coeff(2)
        assert v.Cv == 60.0

    def test_calc_coeff_neg(self):
        v= Valve()
        v.calc_coeff(-2)
        assert v.Cv == 60.0

    def test_calc_coeff_zero(self):
        v = Valve()
        v.calc_coeff(0)
        assert v.Cv == 0.0

    def test_calc_coeff_str(self):
        """Checks for correct Exception thrown if non-number argument used"""
        v = Valve()
        with pytest.raises(TypeError):
            v.calc_coeff("a")


class TestValvePress:
    # x = (flow / self.Cv)
    # self.deltaP = math.pow(x, 2) * spec_grav
    def test_press_drop_expected(self):
        v = Valve(flow_coeff=15.0, sys_flow_out=100)
        v.press_drop(v.flow_out)
        assert v.deltaP == 44.44444444444445

    def test_press_drop_zero(self):
        v = Valve(flow_coeff=15.0)
        v.press_drop(0)
        assert v.deltaP == 0

    def test_press_drop_neg(self):
        v = Valve(flow_coeff=15.0, sys_flow_out=-100)
        v.press_drop(v.flow_out)
        assert v.deltaP == 44.44444444444445

    def test_press_drop_str(self):
        """Checks for correct Exception thrown if non-number argument used"""
        v = Valve(flow_coeff=15.0)
        with pytest.raises(TypeError):
            v.deltaP("a")


class TestValveFlow:
    # x = spec_grav / press_drop
    # self.flow_out = flow_coeff / math.sqrt(x)
    def test_sys_flow_rate_expected(self):
        v = Valve(flow_coeff=15.0, drop=7.5)
        v.valve_flow_out(v.Cv, v.deltaP)
        assert v.flow_out == 41.07919181288746

    def test_sys_flow_rate_zero_coeff(self):
        v = Valve(flow_coeff=0.0, drop=7.5)
        with pytest.raises(ValueError) as excinfo:
            v.valve_flow_out(v.Cv, v.deltaP)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Input values must be > 0."

    def test_sys_flow_rate_zero_press(self):
        v = Valve(flow_coeff=7.5, drop=0.0)
        with pytest.raises(ValueError) as excinfo:
            v.valve_flow_out(v.Cv, v.deltaP)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Input values must be > 0."

    def test_sys_flow_rate_neg_coeff(self):
        v = Valve(flow_coeff=-30.0)
        with pytest.raises(ValueError) as excinfo:
            v.valve_flow_out(v.Cv, v.deltaP)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Input values must be > 0."

    def test_sys_flow_rate_neg_press(self):
        v = Valve(drop=-30.0)
        with pytest.raises(ValueError) as excinfo:
            v.valve_flow_out(v.Cv, v.deltaP)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "Input values must be > 0."

    def test_sys_flow_rate_str_press(self):
        with pytest.raises(ValueError):
            v = Valve(drop="a")

    def test_sys_flow_rate_str_coeff(self):
        with pytest.raises(ValueError):
            v = Valve(flow_coeff="a")


class TestValvePosition:
    def test_cls_get_position(self):
        v = Valve()
        assert v.position == 0

    def test_cls_change_position(self):
        v = Valve()
        v.position = 100
        assert v.position == 100

    def test_open(self):
        v = Valve()
        v.open()
        assert v.position == 100

    def test_close(self):
        v = Valve(position=100)
        v.close()
        assert v.position == 0
