    def read_position(self):
        """Identify the status of the valve."""
        if self.position == 0:
            return "{name} is closed.".format(name=self.name)
        elif self.position == 100:
            return "{name} is open.".format(name=self.name)
        else:   # bad condition
            return "Warning! {name} is partially open.".format(name=self.name)

    def set_open_pressure(self, open_set):
        """Set the pressure setpoint where the valve opens."""
        self.setpoint_open = open_set

    def read_open_pressure(self):
        """Read the high pressure setpoint."""
        return self.setpoint_open
