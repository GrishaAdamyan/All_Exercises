def print_statistics(arr):
    arr.sort()
    if len(arr) != 0:
        erkarutyun = len(arr)
        mijin = sum(arr) / len(arr)
        minimum = min(arr)
        maximum = max(arr)
        if len(arr) % 2 == 1:
            mijnativ = arr[len(arr) // 2]
        else:
            mijnativ = (arr[(len(arr) // 2) - 1] + arr[len(arr) // 2]) / 2
    else:
        erkarutyun = 0
        mijin = 0
        minimum = 0
        maximum = 0
        mijnativ = 0
    print(erkarutyun, mijin, minimum, maximum, mijnativ, sep='\n')


print_statistics([1, 2, 3])