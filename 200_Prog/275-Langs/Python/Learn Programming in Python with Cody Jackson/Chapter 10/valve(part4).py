        Specific gravity of water is 1.

        :param flow_out: System flow rate into the valve
        :param spec_grav: Fluid specific gravity; default assumes fluid is water

        :except ZeroDivisionError: Valve coefficient not provided

        :return: Update pressure drop across valve
        :rtype: float
        """
        
    def valve_flow_out(self, flow_coeff, press_drop, spec_grav=1.0):
        """Calculate the system flow rate through a valve, given a pressure drop.

        Flow rate = valve coefficient / sqrt(spec. grav. / press. drop)
