class GrandChild(Child):
    def __init__(self, value):
        self.data = value
    def __add__(self, new_value):
        return GrandChild(self.data + new_value)
    def __mul__(self, new_value):
        self.data = self.data * new_value
