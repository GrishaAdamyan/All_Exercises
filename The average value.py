def print_average(arr):
    if len(arr) == 0:
        print(0)
    else:
        print(sum(arr) / len(arr))


print_average([1,2,3])