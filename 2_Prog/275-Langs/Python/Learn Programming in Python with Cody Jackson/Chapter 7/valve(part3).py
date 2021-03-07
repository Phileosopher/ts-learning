    def calc_coeff(self, diameter):
        """Roughly calculate Cv based on valve diameter."""
        self.Cv = 15 * math.pow(diameter, 2)

    def press_drop(self, flow_out, spec_grav=1.0):
        """Calculate the pressure drop across a valve, given a flow rate.

        Pressure drop = ((system flow rate / valve coefficient) ** 2) * spec. gravity of fluid Cv of valve and flow rate of system must be known.

        Specific gravity of water is 1.
		"""
        try:
            x = (flow_out / self.Cv)
            self.deltaP = math.pow(x, 2) * spec_grav
        except ZeroDivisionError:
            return "The valve coefficient must be > 0."
