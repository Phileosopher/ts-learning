    def get_press_str(self):
        """Get the current output pressure for the pump."""
        return "The pump pressure is {press:.2f} psi.".format(press=self.outlet_pressure)

    def get_power_str(self):
        """Get the current power draw for the pump."""
        return "The power usage for the pump is {pow:.2f} kW.".format(pow=self.power)
