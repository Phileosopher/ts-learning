# 6.7 - Queue
class client:
    RETAIL = 100
    COMMERCIAL = 101
    def __init__ (self, n, c, t, s):
        self.name = n
        self.category = c
        self.time = t
        self.service = s

class queue:
    def __init__(self):
        self.q = ()
        self.size = 0

    def into (self, c):
        self.q = self.q + (c, )
        self.size = self.size + 1
        print ("INTO: adding :", c.name, " size now ", self.size)

    def out (self):
        if self.size <= 0:
            return None
        result = self.q[0]
        self.q = self.q[1:]
        self.size = self.size - 1
        print ("Removing ", result.name, " size now ", self.size)
        return result

    def empty(self):
        return (self.size <= 0)

c0 = client ("A", client.RETAIL, 0, 0)
c1 = client ("B", client.RETAIL, 1, 0)
c2 = client ("C", client.RETAIL, 2, 0)
c3 = client ("D", client.RETAIL, 3, 0)
c4 = client ("E", client.RETAIL, 4, 0)
c5 = client ("F", client.RETAIL, 5, 0)
c6 = client ("G", client.RETAIL, 6, 0)
c7 = client ("H", client.RETAIL, 7, 0)
q = queue()

q.into (c0)
q.into (c1)
p = q.out()
print (p.name)
p = q.out()
print ("Empty now? ", q.empty())
q.out()
