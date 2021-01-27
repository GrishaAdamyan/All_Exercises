def sumUpNumbers(inputString):
    numbers = '0123456789'
    summ = 0
    j = 0
    for i in range(len(inputString)):
        if i >= j:
            if inputString[i] in numbers:
                j = i
                while j < len(inputString) and inputString[j] in numbers:
                    j += 1
                summ += int(inputString[i:j])
                i = j
    return summ


print(sumUpNumbers("2 apples, 12 oranges"))