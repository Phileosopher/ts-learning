class Dog():
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def dog_age(self):
        return self.age

    def breed(self):
        return self.breed

    @staticmethod
    def howl():
        return "Aroooo!"

    @classmethod
    def type(cls):
        if cls.__name__ == "Dog":
            return "It's a mutt."
        else:
            return cls.__name__

    def __repr__(self):
        return "{breed}, {age}".format(breed = self.breed(), age = self.age)
