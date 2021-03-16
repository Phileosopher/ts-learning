    def open(self):
        """Open the valve"""
        self.__position = 100
        self.flow_out = self.flow_in
        self.press_out = self.press_in

    def close(self):
        """Close the valve"""
        self.__position = 0
        self.flow_out = 0
        self.press_out = 0
        self.deltaP = 0
