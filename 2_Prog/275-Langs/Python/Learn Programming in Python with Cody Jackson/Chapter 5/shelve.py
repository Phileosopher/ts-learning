import shelve
db = shelve.open("shelf.db")
your_list = [1, 2, 3, 4]
db["strings"] = my_list
db["nums"] = your_list
words = db["strings"]
numbers = db["nums"]
