def sudoku2(grid):
    list1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i].count(grid[i][j]) != 1 and grid[i][j] in list1:
                return False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[j].count(grid[j][i]) != 1 and grid[j][i] in list1:
                return False
    list_for_main_diaganal = []
    for i in range(len(grid)):
        list_for_main_diaganal.append(grid[i][i])
    for i in range(len(list_for_main_diaganal)):
        if list_for_main_diaganal.count(list_for_main_diaganal[i]) != 1 and list_for_main_diaganal in list1:
            return False
    list_for_second_diaganal = []
    for i in range(len(grid)):
        list_for_main_diaganal.append(grid[i][9 - 1 - i])
    for i in range(len(list_for_second_diaganal)):
        if list_for_second_diaganal.count(list_for_second_diaganal[i]) != 1 and list_for_second_diaganal in list1:
            return False
    return True


print(sudoku2([[".",".","4",".",".",".","6","3","."], 
               [".",".",".",".",".",".",".",".","."], 
               ["5",".",".",".",".",".",".","9","."], 
               [".",".",".","5","6",".",".",".","."], 
               ["4",".","3",".",".",".",".",".","1"], 
               [".",".",".","7",".",".",".",".","."], 
               [".",".",".","5",".",".",".",".","."], 
               [".",".",".",".",".",".",".",".","."], 
               [".",".",".",".",".",".",".",".","."]]))