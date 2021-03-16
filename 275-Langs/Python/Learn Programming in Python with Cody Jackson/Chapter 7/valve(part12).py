    def read_close_pressure(self):
        """Read the low pressure setpoint."""
        return self.setpoint_close

    def set_close_press(self, close_set):
        """Set the pressure setpoint where the valve closes."""
        self.setpoint_close = close_set

    def valve_operation(self, press_in):
        """Open the valve if pressure is too high; close the valve when pressure lowers."""
        if press_in >= self.setpoint_open:
            self.open()
        elif press_in <= self.setpoint_close:
            self.close()
