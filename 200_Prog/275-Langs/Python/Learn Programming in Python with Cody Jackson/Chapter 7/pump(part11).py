    def adjust_speed(self, new_speed):
        """Defines pump characteristics that are based on pump speed.

        Only applies to variable displacement (centrifugal) pumps. Variable names match pump law equations.
		"""
        n2 = new_speed  # Validate input

        if self.speed == 0:  # Pump initially stopped
            n1 = 1
        else:
            n1 = self.speed
        v1 = self.flow
        hp1 = self.outlet_pressure

        self.flow = v1 * (n2 / n1)  # New flow rate
        self.outlet_pressure = hp1 * math.pow((n2 / n1), 2)  # New outlet pressure
        self.speed = n2  # Replace old speed with new value
        delta_p = self.diff_press_psi(self.head_in, utility_formulas.press_to_head(self.outlet_pressure))
        self.power = self.pump_power(self.flow, delta_p)
