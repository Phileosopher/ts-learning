class CentrifPump(Pump):
    """Defines a variable-displacement, centrifugal-style pump."""

    def get_speed_str(self):
        """Get the current speed of the pump, in rpm."""
        if self.speed == 0:
            return "The pump is stopped."
        else:
            return "The pump is running at {speed} rpm.".format(speed=self.speed)

    def get_flow_str(self):
        """Get the current flow rate of the pump."""
        return "The pump output flow rate is {flow} gpm.".format(flow=self.flow)
