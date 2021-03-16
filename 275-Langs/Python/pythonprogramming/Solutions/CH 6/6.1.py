# 6.1 Class square
class square:
    def __init__ (self, s):
        self.width = s
    def area (self):
        return self.width*self.width

s = square (12)
print (s.area())
