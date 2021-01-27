def average(values):
    if len(values) == 0:
        return 0
    else:
        return sum(values) / len(values)


print(average([1, 2, 3, 4, 5]))