        :param flow_coeff: Valve flow coefficient
        :param press_drop: Pressure drop (psi)
        :param spec_grav: Fluid specific gravity

        :except ValueError: Valve coefficient or deltaP <= 0

        :return: Update system flow rate
        :rtype: float
        """
        
    def get_press_out(self, press_in):
        """Get the valve outlet pressure, calculated from inlet pressure.

        :param press_in:  Pressure at valve inlet
