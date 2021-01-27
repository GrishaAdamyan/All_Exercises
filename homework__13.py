# 1
def same_string(str1, str2):
    return sorted(str1) == sorted(str2)


print(same_string('abvdj', 'vjdab'))

# 2
def search_in_sorted_matrix(matrix, num):
    i = 0
    j = 0
    while i < len(matrix) and j < len(matrix[i]):
        if matrix[i][j] == num:
            return (i, j)
        elif j == len(matrix[i]) - 1:
            j = 0
            i += 1
        else:
            j += 1
    return False


print(search_in_sorted_matrix([[10, 20, 30, 40],
                               [15, 25, 35, 45],
                               [27, 29, 37, 48],
                               [32, 33, 39, 50]],29))