mylist = ["one", "two", "three"]
for item in mylist:
    print("number" + item)

# The following include print() to function properly
print([item for item in mylist])
print(["number " + item for item in mylist])

