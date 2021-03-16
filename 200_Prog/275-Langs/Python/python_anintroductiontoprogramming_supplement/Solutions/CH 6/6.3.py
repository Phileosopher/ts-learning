# 6.3 Client.
class client:
    RETAIL = 100
    COMMERCIAL = 101
    def __init__ (self, n, c, t, s):
        self.name = n
        self.category = c
        self.time = t
        self.service = s

class retail (client):
    def __init__ (self, n, t, s):
        super().__init__ (n, self.RETAIL, t, s)


class commercial (client):
    def __init__ (self, n, t, s):
        super().__init__ (n, self.COMMERCIAL, t, s)


x = client ("Smith", client.RETAIL, 0, 12)
print ("X", x.name, x.category, x.time, x.service)
y = retail ("Smith", 0, 12)
print ("Y", y.name, y.category, y.time, y.service)
z = commercial ("Smith", 0, 12)
print ("z", z.name, z.category, z.time, z.service)