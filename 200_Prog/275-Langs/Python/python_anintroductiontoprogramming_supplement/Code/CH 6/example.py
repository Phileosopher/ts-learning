class person:
    def __init__ (self, name):
        self.name = name
    def introduce (self):
        print ("Hi, my name is ", self.name)
        self.introductions = True

me = person("Jim")
me.introduce()
print (me.introductions)
