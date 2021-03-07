for i in range(2, 20):
    for x in range(2, i):
        if i % x == 0:
            print("{} equals {} * {}".format(i, x, i/x))
            break
    else:
        print("{} is a prime number".format(i))
