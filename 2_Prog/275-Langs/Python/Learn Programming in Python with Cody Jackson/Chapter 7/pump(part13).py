class PositiveDisplacement(Pump):
    """Defines a positive-displacement pump."""

    def __init__(self, name="", flow_rate_out=0.0, pump_head_in=0.0, press_out=0.0, pump_speed=0, displacement=0.0):
        super(PositiveDisplacement, self).__init__(name, flow_rate_out, pump_head_in, press_out, pump_speed)
        self.displacement = displacement

    def get_speed_str(self):
        """Get the current speed of the pump, in rpm."""
        if self.speed == 0:
                return "The pump is stopped."
        else:
            return "The pump is running at {speed} rpm.".format(speed=self.speed)
