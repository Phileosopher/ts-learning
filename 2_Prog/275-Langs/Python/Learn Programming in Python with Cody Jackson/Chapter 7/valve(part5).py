    def get_press_out(self, press_in):
        """Get the valve outlet pressure, calculated from inlet pressure."""
        if press_in:
            self.press_in = press_in  # In case the valve initialization didn't include it, or the value has changed
        self.press_drop(self.flow_out)
        self.press_out = self.press_in - self.deltaP

    @property
    def position(self):
        """Get position of valve, in percent open."""
        return self.__position
