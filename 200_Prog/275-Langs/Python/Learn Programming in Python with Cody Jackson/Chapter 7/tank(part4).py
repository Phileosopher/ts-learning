    @property
    def level(self):
        """Return fluid level in tank."""
        return self.__level

    @level.setter
    def level(self, level):
        """Set the level in the tank."""
        try:
            if not isinstance(level, numbers.Number):
                raise TypeError("Numeric values only.")
            elif level <= 0:
                self.__level = 0.0
            else:
                self.__level = level
        except TypeError:
            raise  # Re-raise error for testing
        finally:
            self.static_tank_press = self.level
            self.gravity_flow(self.pipe_diam, self.pipe_slope, self.pipe_coeff)
