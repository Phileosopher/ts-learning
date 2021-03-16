class Pump:
    """Generic class for pumps.

    Displacement is the amount of fluid pushed through the pump per second.
    Horsepower coefficient is the slope of the equivalent pump curve.
	"""
    def __init__(self, name="", flow_rate_out=0.0, pump_head_in=0.0, press_out=0.0, pump_speed=0):
        """Set initial parameters."""
        self.name = name
        self.__flow_rate_out = float(flow_rate_out)
        self.head_in = float(pump_head_in)
        self.__outlet_pressure = float(press_out)
        self.__speed = pump_speed
        self.__wattage = self.pump_power(self.__flow_rate_out, self.diff_press_psi(self.head_in, self.outlet_pressure))
