class Parent:
    def set_data(self, value):
        self.data = value
    def display(self):
        print(self.data)

class Child(Parent):
    def display(self):
        print("My value is {}".format(self.data))
