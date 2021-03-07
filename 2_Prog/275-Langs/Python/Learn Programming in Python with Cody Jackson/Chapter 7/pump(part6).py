    @flow.setter
    def flow(self, flow_rate):
        """Set the pump outlet flow."""
        self.__flow_rate_out = flow_rate

    @property
    def power(self):
        """Get the current power draw of the pump."""
        return self.__wattage

    @power.setter
    def power(self, power):
        """Set the pump power."""
        self.__wattage = power
