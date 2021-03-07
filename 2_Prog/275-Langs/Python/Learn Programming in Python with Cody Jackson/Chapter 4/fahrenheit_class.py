class Fahrenheit:
    def __init__(self, temp=72):
        self.temp = temp

    def to_celsius(self):
        return (self.temp - 32) / 1.8
