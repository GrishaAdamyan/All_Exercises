#import chess
#print(chess.Board())
matrix_for_chess = [[['r', 'b'], ['n', 'b'], ['e', 'b'], ['q', 'b'], ['k', 'b'], ['e', 'b'], ['n', 'b'], ['r', 'b']],
                    [['p', 'b'], ['p', 'b'], ['p', 'b'], ['p', 'b'], ['p', 'b'], ['p', 'b'], ['p', 'b'], ['p', 'b']],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    ['.', '.', '.', '.', '.', '.', '.', '.'],
                    [['p', 'w'], ['p', 'w'], ['p', 'w'], ['p', 'w'], ['p', 'w'], ['p', 'w'], ['p', 'w'], ['p', 'w']],
                    [['r', 'w'], ['n', 'w'], ['e', 'w'], ['q', 'w'], ['k', 'w'], ['e', 'w'], ['n', 'w'], ['r', 'w']]]
#letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#for elem in matrix_for_chess:
    #for el in elem:
        #print(el, end=' ')
    #print()
#print()
#WHITE_POSITIONS = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2']
#BLACK_POSITIONS = ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8']
#white_pos = input("White side. Enter figure's position: ")
#while white_pos not in WHITE_POSITIONS:
    #white_pos = input("False side. Enter figure's position: ")
#matrix_for_queen = []
#for i in range(len(matrix_for_chess)):
    #matrix_for_queen.append([])
    #for j in range(len(matrix_for_chess[i])):
        #if matrix_for_chess[i][j] == ['q', 'w']:
            #matrix_for_queen[i].append('Q')
        #elif 'w' in matrix_for_chess[i][j]:
            #matrix_for_queen[i].append('w')
        #elif 'b' in matrix_for_chess[i][j]:
            #matrix_for_queen[i].append('b')
        #else:
            #matrix_for_queen[i].append(0)
#for elem in matrix_for_queen:
    #for el in elem:
        #print(el, end=' ')
    #print()
#queen_possible_steps = []
#def add_queen_possible_steps(chess_board):
    #list1 = []
    #flag = False
    #for i in range(len(chess_board)):
        #for j in range(len(chess_board[i])):
            #if chess_board[i][j] == 'Q':
                #flag = True
                #list1.append(i)
                #list1.append(j)
        #if flag:
            #break
    #i = list1[0] - 1
    #j = list1[1]
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #i -= 1
        #if i == - 1:
            #break
    #i = list1[0] + 1
    #j = list1[1]
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #i += 1
        #if i == 8:
            #break       
    #i = list1[0]
    #j = list1[1] - 1
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #j -= 1
        #if j == - 1:
            #break      
    #i = list1[0]
    #j = list1[1] + 1
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #j += 1
        #if j == 8:
            #break       
    #i = list1[0] - 1
    #j = list1[1] - 1
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #i -= 1
            #j -= 1
        #if j == - 1 or i == - 1:
            #break       
    #i = list1[0] + 1
    #j = list1[1] - 1
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #i += 1
            #j -= 1
        #if j == 8 or i == 8:
            #break       
    #i = list1[0] - 1
    #j = list1[1] + 1
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #i -= 1
            #j += 1
        #if j == 8 or i == - 1:
            #break
    #i = list1[0] + 1
    #j = list1[1] + 1
    #while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != 'w':
        #if chess_board[i][j] == 'b':
            #queen_possible_steps.append([i, j])
            #break
        #else:
            #queen_possible_steps.append([i, j])
            #i += 1
            #j += 1
        #if j == 8 or i == 8:
            #break
    #return queen_possible_steps
#print(add_queen_possible_steps(matrix_for_queen))

class Queen:
    def __init__(self, color, cords):
        self.color = color
        self.cords = cords
    
    def possible_steps(self):
        color = ('W', 'B') if self.color == 'B' else ('B', 'W')
        matrix_for_queen = []
        for i in range(len(matrix_for_chess)):
            matrix_for_queen.append([])
            for j in range(len(matrix_for_chess[i])):
                if matrix_for_chess[i][j] == ['q', 'w']:
                    matrix_for_queen[i].append('Q')
                elif 'w' in matrix_for_chess[i][j]:
                    matrix_for_queen[i].append('W')
                elif 'b' in matrix_for_chess[i][j]:
                    matrix_for_queen[i].append('B')
                else:
                    matrix_for_queen[i].append(0)
        queen_possible_steps = []
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
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                i -= 1
            if i == - 1:
                break
        i = list1[0] + 1
        j = list1[1]
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                i += 1
            if i == 8:
                break       
        i = list1[0]
        j = list1[1] - 1
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                j -= 1
            if j == - 1:
                break      
        i = list1[0]
        j = list1[1] + 1
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                j += 1
            if j == 8:
                break       
        i = list1[0] - 1
        j = list1[1] - 1
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                i -= 1
                j -= 1
            if j == - 1 or i == - 1:
                break       
        i = list1[0] + 1
        j = list1[1] - 1
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                i += 1
                j -= 1
            if j == 8 or i == 8:
                break       
        i = list1[0] - 1
        j = list1[1] + 1
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                i -= 1
                j += 1
            if j == 8 or i == - 1:
                break
        i = list1[0] + 1
        j = list1[1] + 1
        while 0 <= i <= 7 and 0 <= j <= 7 and chess_board[i][j] != color[0]:
            if chess_board[i][j] == color[1]:
                queen_possible_steps.append([i, j])
                break
            else:
                queen_possible_steps.append([i, j])
                i += 1
                j += 1
            if j == 8 or i == 8:
                break
        return queen_possible_steps
w_q = Queen('W', [7, 3])
print(w_q.possible_steps)