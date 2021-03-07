    @property
    def outlet_pressure(self):
        """Get the current outlet pressure of the pump."""
        return self.__outlet_pressure

    @outlet_pressure.setter
    def outlet_pressure(self, press):
        """Set the pump outlet pressure."""
        self.__outlet_pressure = press

    @property
    def flow(self):
        """Get the current outlet flow rate of the pump."""
        return self.__flow_rate_out
