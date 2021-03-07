from Glib import *

class node:
    def __init__ (self, character, count):
        self.value = character
        self.count = count
        self.left = None
        self.right = None
        self.next = None

    def setLeft (self, n):
        self.left = n

    def setRight (self, n):
        self.right = n

def drawnode (p, x, y, n):
    ellipse (x, y, 30, 30)
    fill (0)
    print ("Drawing ", p.value, p.count, x, y)
    text (p.value+str(p.count), x-6, y+7)
    if p.left != None:
        fill (255, 255, 0)
        line (x, y, x-4.5*n*n, y+100)
        drawnode(p.left, x-4.5*n*n, y+100, n-1)
    if p.right != None:
        fill (255)
        line (x, y, x+4.5*n*n, y+100)
        drawnode (p.right, x+4.5*n*n, y+100, n-1)

heap = []
s = "i think that at that time none of us quite believed in the time machine"
print ("Length", len(s))
c = 0
for i in ('a','b', 'c','d','e','f','g','h','i','k','l',\
    'm','n','o','p','q','r','s','t','u','v','w','x','y','z',' '):
    k = s.count(i)
    if k>0:
        print ("Count of ", i, " is ", k)
        p = node (i, k)
        heap = heap + [p,]
        c = c + k
print (c)

# Now organize the tree
while len(heap) > 1:
    n1 = heap[0]
    for nxt in heap:
        if nxt.count < n1.count:
            n1 = nxt
    heap.remove(n1)
    n2 = heap[0]
    for nxt in heap:
        if nxt.count < n2.count:
            n2 = nxt
    heap.remove(n2)
    nw = node ("", n1.count+n2.count)
    nw.setLeft(n1)
    nw.setRight(n2)
    heap = heap + [nw,]
    print ("New node: Left ", n1.value, " Right ", n2.value, " Count=", nw.count)

startdraw(1050, 800)
background (100, 100, 255)
fill (255)
drawnode (heap[0], 400, 40, 7)
enddraw()

