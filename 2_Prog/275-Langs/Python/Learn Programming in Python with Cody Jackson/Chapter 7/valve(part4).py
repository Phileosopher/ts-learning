    def valve_flow_out(self, flow_coeff, press_drop, spec_grav=1.0):
        """Calculate the system flow rate through a valve, given a pressure drop.

        Flow rate = valve coefficient / sqrt(spec. grav. / press. drop)
		"""
        try:
            if flow_coeff <= 0 or press_drop <= 0:
                raise ValueError("Input values must be > 0.")
            else:
                x = spec_grav / press_drop
                self.flow_out = flow_coeff / math.sqrt(x)
                return self.flow_out
        except ValueError:
            raise  # Re-raise error for testing
