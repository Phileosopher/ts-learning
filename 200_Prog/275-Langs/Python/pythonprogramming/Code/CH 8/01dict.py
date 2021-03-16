colors = {'red':(255, 0, 0), 'blue':(0,0,255), 'green':(0,255,0)}

print (colors['blue'])
colors['khaki'] = (240,230,140)
colors['cornflower'] = (100,149,237)
del(colors['blue'])
for s in colors:
    print(colors[s])
print(list(colors.keys()))


c = {}
c[(255,0,0)] = 'red'
print (c[255, 0, 0])