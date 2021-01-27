def arrayMaxConsecutiveSum(inputArray, k):
    start, end = 0, k - 1
    max = 0
    while end < len(inputArray):
        if max < sum(inputArray[start:end + 1]):
            max = sum(inputArray[start:end + 1])
        start += 1
        end += 1
    return max


print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))