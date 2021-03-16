import pickle
my_list = ["one", "two", "a", "bucket", "of", "spam"]
save_file = open("pickle_rick", "wb")
pickle.dump(my_list, save_file)
save_file.close()
open_file = open("pickle_rick", "rb")
pickled_rick = pickle.load(open_file)
print(pickled_rick)
