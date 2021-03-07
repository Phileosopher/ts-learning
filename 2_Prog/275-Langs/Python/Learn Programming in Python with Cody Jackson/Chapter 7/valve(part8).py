class Gate(Valve):
    """Open/closed valve."""
    def read_position(self):
        """Identify the position of the valve."""
        if self.position == 0:
            return "{name} is closed.".format(name=self.name)
        elif self.position == 100:
            return "{name} is open.".format(name=self.name)
        else:  # bad condition
            return "Warning! {name} is partially open.".format(name=self.name)

    def turn_handle(self, new_position):
        """Change the status of the valve."""
        if new_position == 0:
            self.close()
        elif new_position == 100:
            self.open()
        else:  # Shouldn't get here
            return "Warning: Invalid valve position."
