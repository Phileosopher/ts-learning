    def adjust_speed(self, new_speed):
        """Modify the speed of the pump, assuming constant outlet pressure.

        Affects the outlet flow rate and power requirements for the pump.
		"""
        self.speed = new_speed
        press_in = utility_formulas.head_to_press(self.head_in)

        self.flow = self.speed * self.displacement
        self.power = self.pump_power(self.flow, self.diff_press_psi(press_in, self.outlet_pressure))
# TODO: Account for different flow rates based on outlet pressure
