# 1
#list1 = [2,-1,1,5,4,-1,3]
#list2 = []
#for i in range(len(list1)):
    #if list1[i] != -1:
        #list2.append(list1[i])
#list2.sort()
#for i in range(len(list1)):
    #if list1[i] == -1:
        #list2.insert(i,-1)
#print(list2)

# 2
matrix = [[0, 0, 0, 10, 'w', 'f', 0, 'w', 'f', 0],
          [0, 0, 0, 'w', 'w', 'f', 10, 0, 'w', 'f'],
          ['w', 'f', 'f', 'f', 'f', 'w', 0, 'w', 0, 0],
          ['w', 'f', 'f', 'f', 'f', 0, 0, 0, 'w', 'w'],
          [0, 0, 0, 0, 'f', 'f', 'f', 'f', 'w', 'f'],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
count = 0
for i in range(len(matrix)):
    if count == 0 and 10 in matrix[i]:
        count += 1
        tup1 = i, matrix[i].index(10)
    elif count == 1 and 10 in matrix[i]:
        count += 1
        tup2 = i, matrix[i].index(10)
    elif count == 2:
        break


def get_animal_1_steps(matrix):
    neighbours1 = []
    for i in range(tup1[0] - 1,tup1[0] + 2):
        if 0 <= i < 10:
            for j in range(tup1[1] - 1,tup1[1] + 2):
                if 0 <= j < 10 and (i, j) != tup1:
                    neighbours1.append((i, j))
    print(neighbours1)

get_animal_1_steps(matrix)

def get_animal_2_steps(matrix):
    neighbours2 = []
    for i in range(tup2[0] - 1,tup2[0] + 2):
        if 0 <= i < 10:
            for j in range(tup2[1] - 1,tup2[1] + 2):
                if 0 <= j < 10 and (i, j) != tup2:
                    neighbours2.append((i, j))
    print(neighbours2)

get_animal_2_steps(matrix)

def get_items_for_1(matrix):
    get_animal_1_steps(matrix)
    for i in range(len(neighbours1)):
        if matrix[neighbours1[i]] == 10:
            if matrix[tup1] - matrix[neighbours1[i]] > 0:
                matrix[tup1] -= matrix[neighbours1[i]]
                matrix[neighbours1[i]] = 'd'
                return
            elif matrix[tup1] - matrix[neighbours1[i]] == 0:
                matrix[tup1] = 'd'
                matrix[neighbours1[i]] = 'd'
                return
            else:
                matrix[tup1] = 'd'
                matrix[neighbours1[i]] -= matrix[tup1]
                return
    else:
        for i in range(len(neighbours1)):
            if matrix[neighbours1[i]] == 'f':
                matrix[tup1] = 0
                matrix[neighbours1[i]] = matrix[tup1] + 1
                return
            elif matrix[neighbours1[i]] == 'w':
                matrix[tup1] = 0
                matrix[neighbours1[i]] = matrix[tup1] + 0.5
                return
        else:
            matrix[tup1] = 0
            matrix[neighbours1[0]] = matrix[tup1] - 1
            return

print(get_items_for_1(matrix))

def get_items_for_2(matrix):
    get_animal_2_steps(matrix)
    for i in range(len(neighbours2)):
        if matrix[neighbours2[i]] == 10:
            if matrix[tup2] - matrix[neighbours2[i]] > 0:
                matrix[tup2] -= matrix[neighbours2[i]]
                matrix[neighbours2[i]] = 'd'
                return
            elif matrix[tup2] - matrix[neighbours2[i]] == 0:
                matrix[tup2] = 'd'
                matrix[neighbours2[i]] = 'd'
                return
            else:
                matrix[tup2] = 'd'
                matrix[neighbours2[i]] -= matrix[tup2]
                return
    else:
        for i in range(len(neighbours2)):
            if matrix[neighbours2[i]] == 'f':
                matrix[tup2] = 0
                matrix[neighbours2[i]] = matrix[tup2] + 1
                return
            elif matrix[neighbours2[i]] == 'w':
                matrix[tup2] = 0
                matrix[neighbours2[i]] = matrix[tup2] + 0.5
                return
        else:
            matrix[tup2] = 0
            matrix[neighbours2[0]] = matrix[tup2] - 1