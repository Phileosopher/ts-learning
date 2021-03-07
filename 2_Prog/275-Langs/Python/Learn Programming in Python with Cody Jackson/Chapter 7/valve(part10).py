class Relief(Valve):
    """Pressure relieving valve.

    Assumes full open when open set point reached and fully closed when close set point reached. Does not affect flow rate or system pressure; those parameters must be adjusted elsewhere.
	"""
    def __init__(self, name="", sys_flow_in=0.0, sys_flow_out=0.0, drop=0.0, position=0, flow_coeff=0.0, press_in=0.0, open_press=0, close_press=0):
        """Inherits base initialization and adds valve open/close pressure values."""
		super(Relief, self).__init__(name, sys_flow_in, sys_flow_out, drop, position, flow_coeff, press_in)
        self.setpoint_open = open_press
        self.setpoint_close = close_press
