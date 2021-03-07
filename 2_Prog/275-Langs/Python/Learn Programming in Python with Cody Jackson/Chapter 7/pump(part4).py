   @property
    def speed(self):
        """Get the current speed of the pump."""
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        """Change the pump speed."""
        try:
            if not isinstance(new_speed, numbers.Number):
                raise TypeError("Numeric values only.")
            elif new_speed < 0:
                raise ValueError("Speed must be 0 or greater.")
            else:
                self.__speed = new_speed
        except TypeError:
            raise  # Re-raise error for testing
        except ValueError:
            raise  # Re-raise error for testing
