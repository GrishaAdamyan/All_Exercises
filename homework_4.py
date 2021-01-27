# 1
def get_neighbours_coords(i_cord, j_cord, matrix_i, matrix_j):
    coords = []
    for i in range(i_cord - 1, i_cord + 2):
        for j in range(j_cord - 1, j_cord + 2):
            if 0 <= i <= matrix_i - 1 and 0 <= j <= matrix_j - 1 and (i, j) != (i_cord, j_cord):
                coords.append((i, j))
    return coords


def minesweeper(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            neighbours_coords = get_neighbours_coords(i, j, len(matrix), len(matrix[i]))
            count = 0
            for coord_x, coord_y in neighbours_coords:
                if matrix[coord_x][coord_y]:
                    count += 1
            new_matrix[i].append(count)
    return new_matrix


# 2
word = input()
t = 1
start, end = 0, 0 + t
vowels = {}
consonants = {}
while t < len(word):
    if word[start] in 'aeyuio':
        vowels[word[start:end]] = vowels.get(word[start:end], 0) + 1
        start += 1
        end += 1
    elif word[start] not in 'aeyuio':
        consonants[word[start:end]] = consonants.get(word[start:end], 0) + 1
        start += 1
        end += 1
    if end == len(word) + 1:
        t += 1
        start = 0
        end = 0 + t
print(vowels, consonants, sep='\n')