def differentSquares(matrix):
    list1 = []
    if len(matrix) <= 1:
        return 0
    elif len(matrix[0]) <= 1:
        return 0
    else:
        m = n = 0
        while m < len(matrix) - 1:
            list1.append([matrix[m][n], matrix[m][n + 1], matrix[m + 1][n], matrix[m + 1][n + 1]])
            n += 1
            if n == len(matrix[m]) - 1:
                m += 1
                n = 0
    count = 0
    i = 0
    while i < len(list1):
        if list1.count(list1[i]) != 1:
            list1.remove(list1[i])
        else:
            list1.remove(list1[i])
            count += 1
    return count