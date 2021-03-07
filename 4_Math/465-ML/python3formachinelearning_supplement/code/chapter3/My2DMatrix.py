
rows = 3
cols = 3

my2DMatrix = [[0 for i in range(rows)] for j in range(rows)]
print('Before:',my2DMatrix)

for row in range(rows):
  for col in range(cols):
    my2DMatrix[row][col] = row*row+col*col
print('After: ',my2DMatrix)

