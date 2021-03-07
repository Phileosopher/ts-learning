    @position.setter
    def position(self, new_position):
        """Change the valve's position.

        If new position is not an integer, an error is raised.
		"""
        try:
            if type(new_position) != int:
                raise TypeError("Integer values only.")
            else:
                self.__position = new_position
        except TypeError:
            raise  # Re-raise for testing
