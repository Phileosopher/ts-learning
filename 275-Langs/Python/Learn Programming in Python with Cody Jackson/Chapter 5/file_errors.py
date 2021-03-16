f = open("afile.txt", "w")
f.write("Hello there, my little friend.\nWill you gracefully fail?")
f.close()

try:
    file = open("afile.txt")
    print(file.read())
    file.close()
except IOError:
    print("The file doesn't exist.")

try:
    file = open("nofile")
    print(file.read())
    file.close()
except IOError:
    print("The file doesn't exist.")

