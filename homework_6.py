# 1
def possible_turns(cell):
    list1 = []
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    if letters.index(letters[-1]) >= letters.index(cell[0]) - 2 >= letters.index(letters[0]) and 1 <= int(cell[1]) + 1 <= 8:
        list1.append((letters[letters.index(cell[0]) - 2]) + str(int(cell[1]) + 1))
    if letters.index(letters[-1]) >= letters.index(cell[0]) - 2 >= letters.index(letters[0]) and 1 <= int(cell[1]) - 1 <= 8:
        list1.append((letters[letters.index(cell[0]) - 2]) + str(int(cell[1]) - 1))
    if letters.index(letters[-1]) >= letters.index(cell[0]) - 1 >= letters.index(letters[0]) and 1 <= int(cell[1]) + 2 <= 8:
        list1.append((letters[letters.index(cell[0]) - 1]) + str(int(cell[1]) + 2))
    if letters.index(letters[-1]) >= letters.index(cell[0]) - 1 >= letters.index(letters[0]) and 1 <= int(cell[1]) - 2 <= 8:
        list1.append((letters[letters.index(cell[0]) - 1]) + str(int(cell[1]) - 2))
    if letters.index(letters[-1]) >= letters.index(cell[0]) + 1 >= letters.index(letters[0]) and 1 <= int(cell[1]) + 2 <= 8:
        list1.append((letters[letters.index(cell[0]) + 1]) + str(int(cell[1]) + 2))
    if letters.index(letters[-1]) >= letters.index(cell[0]) + 1 >= letters.index(letters[0]) and 1 <= int(cell[1]) - 2 <= 8:
        list1.append((letters[letters.index(cell[0]) + 1]) + str(int(cell[1]) - 2))
    if letters.index(letters[-1]) >= letters.index(cell[0]) + 2 >= letters.index(letters[0]) and 1 <= int(cell[1]) -1 <= 8:
        list1.append((letters[letters.index(cell[0]) + 2]) + str(int(cell[1]) - 1))
    if letters.index(letters[-1]) >= letters.index(cell[0]) + 2 >= letters.index(letters[0]) and 1 <= int(cell[1]) + 1 <= 8:
        list1.append((letters[letters.index(cell[0]) + 2]) + str(int(cell[1]) + 1))
    return list1


print(possible_turns('B1'))

# 2
def add_queen_possible_steps(chess_board):
    list1 = []
    flag = False
    for i in range(len(chess_board)):
        for j in range(len(chess_board[i])):
            if chess_board[i][j] == 'Q':
                flag = True
                list1.append(i)
                list1.append(j)
        if flag:
            break
    i = list1[0] - 1
    j = list1[1]
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        i -= 1
        if i == - 1:
            break
    i = list1[0] + 1
    j = list1[1]
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        i += 1
        if i == 8:
            break
    i = list1[0]
    j = list1[1] - 1
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        j -= 1
        if j == - 1:
            break
    i = list1[0]
    j = list1[1] + 1
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        j += 1
        if j == 8:
            break
    i = list1[0] - 1
    j = list1[1] - 1
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        i -= 1
        j -= 1
        if j == - 1 or i == - 1:
            break
    i = list1[0] + 1
    j = list1[1] - 1
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        i += 1
        j -= 1
        if j == 8 or i == 8:
            break
    i = list1[0] - 1
    j = list1[1] + 1
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        i -= 1
        j += 1
        if j == 8 or i == - 1:
            break
    i = list1[0] + 1
    j = list1[1] + 1
    while chess_board[i][j] != 1:
        chess_board[i][j] = 'x'
        i += 1
        j += 1
        if j == 8 or i == 8:
            break
    return chess_board
print(add_queen_possible_steps([[0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 'Q', 0, 0, 0],
                                [0, 0, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0]]))