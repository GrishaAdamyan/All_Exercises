# 1
list1 = [['x', 'emp', 'emp'],
         ['o', 'x', 'emp'],
         ['o','emp', 'x']]

def x_o(list1):
    for i in range(len(list1)):
        if list1[i].count('x') == 3:
            return 'x'
        elif list1[i].count('o') == 3:
            return 'o'
    list2 = [[], [], []]
    for i in range(3):
        for j in range(3):
            list2[i].append(list1[j][i])
    for i in range(len(list2)):
        if list2[i].count('x') == 3:
            return 'x'
        elif list2[i].count('o') == 3:
            return 'o'
    list3 = [[],[]]
    for j in range(3):
        list3[0].append(list1[j][j])
        list3[1].append(list1[j][3 - 1 - j])
    for i in range(len(list3)):
        if list3[i].count('x') == 3:
            return 'x'
        elif list3[i].count('o') == 3:
            return 'o'
    count = [sum(list1[i].count('x') for i in range(len(list1)))] + [sum(list1[i].count('o') for i in range(len(list1)))]
    if count[0] != 9:
        if [sum(list1[i].count('x') for i in range(len(list1)))] < [sum(list1[i].count('o') for i in range(len(list1)))]:
            return 'x'
        else:
            return 'o'
    return -1
print(x_o(list1))

# 2
def tv_progressia(list1):
    list1 = [1, 6, 16, 21, 31]
    for i in range(2, max(list1)):
        for j in range(1, len(list1)):
            if (list1[j] - list1[j - 1]) % i != 0:
                break
            elif (list1[j] - list1[j - 1]) % i == 0 and j == len(list1) - 1:
                return True
    return False
print(tv_progressia(list1))