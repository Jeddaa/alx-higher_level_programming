for i in range(0, 8):
    for j in range (1, 10):
        if i != j and i < j:
            print("{}{}".format(i, j), end=', ')
print("{}{}".format(i + 1, j))
