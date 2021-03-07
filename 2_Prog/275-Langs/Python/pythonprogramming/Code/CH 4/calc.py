# Calculator manufacturing

def profit (s, g):
    return -2*s + 5*g

def searchmax (f, x0, y0, x1, y1, sum):
    pmax = -1.0e12
    ps = -100
    pg = -100
    for s in range (x0, x1+1):
        for g in range (y0, y1+1):
            if s+g >= sum:
                p = f (s, g)
                if p>=pmax:
                    pmax = p
                    ps = s
                    pg = g
    return ( (ps, pg) )

c = searchmax (profit, 100, 80, 200, 170, 200)
print (c)