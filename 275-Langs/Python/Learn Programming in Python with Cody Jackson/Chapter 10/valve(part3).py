    def calc_coeff(self, diameter):
        """Roughly calculate Cv based on valve diameter.

        :param diameter: Valve diameter

        :return: Update valve flow coefficient
        """

    def press_drop(self, flow_out, spec_grav=1.0):
        """Calculate the pressure drop across a valve, given a flow rate.

        Pressure drop = ((system flow rate / valve coefficient) ** 2) * spec. gravity of fluid

        Cv of valve and flow rate of system must be known.
