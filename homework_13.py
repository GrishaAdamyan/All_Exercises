# 1
import copy
def financialCrisis(roadRegister):
    list1 = []
    for i in range(len(roadRegister)):
        list2 = copy.deepcopy(roadRegister)
        del list2[i]
        for k in range(len(list2)):
            del list2[k][i]
        list1.append(list2)
    return list1


print(financialCrisis([[False, True, True, False], 
                       [True, False, True, False], 
                       [True, True, False, True], 
                       [False, False, True, False]]))

# 2
def namingRoads(roads):
    dict1 = {}
    for elem in roads:
        dict1[elem[2]] = (elem[0], elem[1])
    list1 = dict1.keys()
    if len(list1) > 2:
        for i in range(1, max(list1)):
            set1 = {dict1[i][0], dict1[i][1], dict1[i - 1][0], dict1[i - 1][1]}
            if len(set1) != 4:
                return False
        return True
    else:
        for i in range(1, 2):
            set1 = {dict1[i][0], dict1[i][1], dict1[i - 1][0], dict1[i - 1][1]}
            if len(set1) != 4:
                return False
        return True