    def __init__(self, name="", sys_flow_in=0.0, sys_flow_out=0.0, drop=0.0, position=0, flow_coeff=0.0, press_in=0.0):
        """Initialize valve.

        :param sys_flow_out: Fluid flow out of the valve
        :param drop: Pressure drop across the valve
        :param press_in: Pressure at valve inlet
        :param name: Instance name
        :param sys_flow_in: Flow rate into the valve
        :param position: Percentage valve is open
        :param flow_coeff: Affect valve has on flow rate; assumes a 2 inch, wide open valve
        """
