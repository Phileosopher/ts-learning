# Exercise 4.3

def triangle(n):
    print ("  "*(n), end="")
    print (" 1")
    line = [1, 1]
    for i in range(1,n):
        print ("  "*(n-i), end="")
        print (line)
        line=[1]+line
        for j in range(1, len(line)-1):
            line[j] = line[j] + line[j+1]

# Tests
print (triangle(6))
print (triangle(12))

# Explanation:
# first row is 1 so just print it
# second row is [1, 1], so line = [1,1]
#  repeat
#    print line
#    expand list by 1, adding a 1 to the beginning.
#    the rest of the list is now the value of the previous row! So,
#     replace list[1] by list[1]+list[2], list[2] = list[2]+list[3], etc.
# end the repetition when n rows have been printed.
