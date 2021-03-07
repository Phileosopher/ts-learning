        :return: Pressure at valve outlet
        :rtype: float
        """
        
class Gate(Valve):
    """Open/closed valve.

    Subclasses Valve.

    Methods:
        read_position()
        turn_handle()
    """
    def read_position(self):
        """Identify the position of the valve.
