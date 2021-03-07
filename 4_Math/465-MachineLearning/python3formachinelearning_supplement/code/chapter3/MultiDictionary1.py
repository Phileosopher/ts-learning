from collections import defaultdict

d= {'a' : [1, 2, 3], 'b' : [4, 5]}
print('first time:',d)

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print('second time:',d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print('third time:',d)

