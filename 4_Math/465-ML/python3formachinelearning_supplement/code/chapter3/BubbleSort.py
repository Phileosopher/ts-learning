
list1 = [1, 5, 3, 4]

print("Initial list:",list1)

for i in range(0,len(list1)-1):
  for j in range(i+1,len(list1)):
    if(list1[i] > list1[j]):
      temp = list1[i]
      list1[i] = list1[j] 
      list1[j] = temp

print("Sorted list: ",list1)

