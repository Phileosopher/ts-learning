class Fahrenheit:
    def __init__(self, temp=72):
        self.set_temp(temp)

    def to_celsius(self):
        return (self.get_temp() - 32) / 1.8

    def set_temp(self, temp):
        if temp < -459.67:
            raise ValueError("Temperature cannot be less than absolute zero")
        self._temp = temp

    def get_temp(self):
        return self._temp
