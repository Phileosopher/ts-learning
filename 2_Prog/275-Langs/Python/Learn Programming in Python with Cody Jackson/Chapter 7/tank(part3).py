    @property
    def static_tank_press(self):
        """Return hydrostatic tank pressure."""
        return self.__tank_press

    @static_tank_press.setter
    def static_tank_press(self, level):
        """Calculate the static fluid pressure based on tank level."""
        try:
            if not isinstance(level, numbers.Number):
                raise TypeError("Numeric values only.")
            elif level <= 0:
                self.__tank_press = 0.0
            else:
                self.__tank_press = utility_formulas.static_press(self.level, self.fluid_density)
        except TypeError:
            raise  # Re-raise for testing
