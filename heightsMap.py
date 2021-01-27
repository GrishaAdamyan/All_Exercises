def find_mountain(heightsMap):
    x, y = -1, -1
    maxx = -1
    for row in range(len(heightsMap)):
        for col in range(len(heightsMap[row])):
            if heightsMap[row][col] > maxx:
                maxx = heightsMap[row][col]
                x, y = row, col
    return x, y


print(find_mountain([[1, 3, 1], [3, 2, 5], [2, 2, 2]]))