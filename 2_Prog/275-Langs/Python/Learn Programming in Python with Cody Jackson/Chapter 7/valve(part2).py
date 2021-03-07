import math

class Valve:
    """Generic class for valves.

    Cv is the valve flow coefficient: number of gallons per minute at 60F through a fully open valve with a press. drop of 1 psi. For valves 1 inch or less in diameter, Cv is typically < 5.
    """
	def __init__(self, name="", sys_flow_in=0.0, sys_flow_out=0.0, drop=0.0, position=0, flow_coeff=0.0, press_in=0.0):
        """Initialize valve."""
		self.name = name
       self.__position = int(position)  # Truncate float values for ease of calculations
        self.Cv = float(flow_coeff)
        self.flow_in = float(sys_flow_in)
        self.deltaP = float(drop)
        self.flow_out = float(sys_flow_out)
        self.press_out = 0.0
        self.press_in = press_in
