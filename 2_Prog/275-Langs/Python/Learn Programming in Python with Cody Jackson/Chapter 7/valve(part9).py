class Globe(Valve):
    """Throttling valve."""

    def read_position(self):
        """Identify the position of the valve."""
        return "{name} is {position}% open.".format(name=self.name, position=self.position)

    def turn_handle(self, new_position):
        """Change the status of the valve."""
        if new_position == 100:
            self.open()
        elif new_position == 0:
            self.close()
        else:
            self.position = new_position
            self.flow_out = self.flow_in * self.position / 100
            self.press_drop(self.flow_out)
            self.get_press_out(self.press_in)
