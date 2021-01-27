# 1
#letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#a = input()
#b = input()
#print((letters.index(a[0]) + 1 + int(a[1])) % 2 == (letters.index(b[0]) + 1 + int(b[1])) % 2)

# 2
matrix = [[0, 0, 0, 'r', 0, 0, 'ek', 0],
          [0, 'q', 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0]]
def mat(matrix):
    list_for_queen = []
    list_for_rook = []
    list_for_enemy_king = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if -1 < i < 8 and -1 < j < 8:
                if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                    list_for_rook.append(i)
                    list_for_rook.append(j)
                    i = list_for_rook[0] - 1
                    j = list_for_rook[1]
                    while i > - 1:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i -= 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i -= 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i -= 1
                        else:
                            matrix[i][j] = 'x'
                            i -= 1
                    i = list_for_rook[0] + 1
                    j = list_for_rook[1]
                    while i < 8:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i += 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i += 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i += 1
                        else:
                            matrix[i][j] = 'x'
                            i += 1
                    i = list_for_rook[0]
                    j = list_for_rook[1] - 1
                    while j > - 1:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            j -= 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            j -= 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            j -= 1
                        else:
                            matrix[i][j] = 'x'
                            j -= 1
                    i = list_for_rook[0]
                    j = list_for_rook[1] + 1
                    while j < 8:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            j += 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            j += 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            j += 1
                        else:
                            matrix[i][j] = 'x'
                            j += 1
                    list_for_rook = []
                elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                    list_for_queen.append(i)
                    list_for_queen.append(j)
                    i = list_for_queen[0] - 1
                    j = list_for_queen[1]
                    while i > - 1:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i -= 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i -= 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i -= 1
                        else:
                            matrix[i][j] = 'x'
                            i -= 1
                    i = list_for_queen[0] + 1
                    j = list_for_queen[1]
                    while i < 8:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i += 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i += 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i += 1
                        else:
                            matrix[i][j] = 'x'
                            i += 1
                    i = list_for_queen[0]
                    j = list_for_queen[1] - 1
                    while j > - 1:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            j -= 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            j -= 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            j -= 1
                        else:
                            matrix[i][j] = 'x'
                            j -= 1
                    i = list_for_queen[0]
                    j = list_for_queen[1] + 1
                    while j < 8:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            j += 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            j += 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            j += 1
                        else:
                            matrix[i][j] = 'x'
                            j += 1
                    i = list_for_queen[0] - 1
                    j = list_for_queen[1] - 1
                    while i > - 1 and j > - 1:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i -= 1
                            j -= 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i -= 1
                            j -= 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i -= 1
                            j -= 1
                        else:
                            matrix[i][j] = 'x'
                            i -= 1
                            j -= 1
                    i = list_for_queen[0] + 1
                    j = list_for_queen[1] - 1
                    while i < 8 and j > - 1:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i += 1
                            j -= 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i += 1
                            j -= 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i += 1
                            j -= 1
                        else:
                            matrix[i][j] = 'x'
                            i += 1
                            j -= 1
                    i = list_for_queen[0] - 1
                    j = list_for_queen[1] + 1
                    while i > - 1 and j < 8:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i -= 1
                            j += 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i -= 1
                            j += 1
                        elif matrix[i][j] == 'ek'or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i -= 1
                            j += 1
                        else:
                            matrix[i][j] = 'x'
                            i -= 1
                            j += 1
                    i = list_for_queen[0] + 1
                    j = list_for_queen[1] + 1
                    while i < 8 and j < 8:
                        if matrix[i][j] == 'r' or matrix[i][j] == 'rx':
                            matrix[i][j] = 'rx'
                            i += 1
                            j += 1
                        elif matrix[i][j] == 'q' or matrix[i][j] == 'qx':
                            matrix[i][j] = 'qx'
                            i += 1
                            j += 1
                        elif matrix[i][j] == 'ek' or matrix[i][j] == 'ekx':
                            matrix[i][j] = 'ekx'
                            i += 1
                            j += 1
                        else:
                            matrix[i][j] = 'x'
                            i += 1
                            j += 1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'ekx':
                if -1 < i-1 and i-1 < 8 and -1 < j-1 and j-1 < 8:
                    if not matrix[i-1][j-1] == 'x' or matrix[i-1][j-1] == 'rx' or matrix[i-1][j-1] == 'qx':
                        return 'Matayin dirq che'
                if -1 < i and i < 8 and -1 < j-1 and j-1 < 8:
                    if not matrix[i][j-1] == 'x' or matrix[i][j-1] == 'rx' or matrix[i][j-1] == 'qx':
                        return 'Matayin dirq che'
                if -1 < i+1 and i+1 < 8 and -1 < j-1 and j-1 < 8:
                    if not matrix[i+1][j-1] == 'x' or matrix[i+1][j-1] == 'rx' or matrix[i+1][j-1] == 'qx':
                        return 'Matayin dirq che'
                if -1 < i-1 and i-1 < 8 and -1 < j and j < 8:
                    if not matrix[i-1][j] == 'x' or matrix[i-1][j] == 'rx' or matrix[i-1][j] == 'qx':
                        return 'Matayin dirq che'
                if -1 < i+1 and i+1 < 8 and -1 < j and j < 8:
                    if not matrix[i+1][j] == 'x' or matrix[i+1][j] == 'rx' or matrix[i+1][j] == 'qx':
                        return 'Matayin dirq che'
                if -1 < i-1 and i-1 < 8 and -1 < j+1 and j+1 < 8:
                    if not matrix[i-1][j+1] == 'x' or matrix[i-1][j+1] == 'rx' or matrix[i-1][j+1] == 'qx':
                        return 'Matayin dirq che'
                if -1 < i and i < 8 and -1 < j+1 and j+1 < 8:
                    if not matrix[i][j+1] == 'x' or matrix[i][j+1] == 'rx' or matrix[i][j+1] == 'qx':
                        return 'Matayin dirq che'
                if -1 < i+1 and i+1 < 8 and -1 < j+1 and j+1 < 8:
                    if not matrix[i+1][j+1] == 'x' or matrix[i+1][j+1] == 'rx' or matrix[i+1][j+1] == 'qx':
                        return 'Matayin dirq che'
                return 'Matayin dirq e'
print(mat(matrix))