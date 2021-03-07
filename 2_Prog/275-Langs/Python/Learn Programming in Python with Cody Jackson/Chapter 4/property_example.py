class Fahrenheit:
    def __init__(self, temp=72):
        self._temp = temp

    def to_celsius(self):
        return (self._temp - 32) / 1.8

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, value):
        if value < -459.67:
            raise ValueError("Temperature cannot be less than absolute zero")
        self._temp = value