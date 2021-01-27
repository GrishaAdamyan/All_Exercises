# 1
def arrayMaximalDifference(inputArray):
    max = 0
    for i in range(1, len(inputArray)):
        if abs(inputArray[i] - inputArray[i - 1]) > max:
            max = abs(inputArray[i] - inputArray[i - 1])
    return max


print(arrayMaximalDifference([5, 9, 2, 12, 5, 8]))

# 2
def get_count_2(n):
    count = 0
    for i in range(1, n + 1):
        list1 = list(str(i))
        count += list1.count('2')
    return count


print(get_count_2(12))