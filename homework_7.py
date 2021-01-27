# 1
list1 = [1, 4, 6, 5, 7, 10]
def swap_list_elements(list1):
    l = 0
    r = len(list1)-1
    while l < r:
        while l != len(list1) and list1[l] % 2 == l % 2:
            l += 1
        while r != 0 and list1[r] % 2 == r % 2:
            r -= 1
        if l < r:
            list1[l], list1[r] = list1[r], list1[l]
    return list1


print(swap_list_elements(list1))

# 2
dict_of_points = {'A': (0, 0), 'B': (0, 4), 'C': (2, 0), 'D': (2, 4), 'E': (0, -4), 'F': (2, -4)}
def get_count_of_rectangles(dict_of_points):
    list1 = list(dict_of_points.keys())
    list2 = list(dict_of_points.values())
    set1 = set()
    for i in range(len(list2)):
        for j in range(i + 1, len(list2)):
            if (list2[i][0], list2[j][1]) in list2[:i] + list2[i + 1:j] + list2[j + 1:] and (list2[j][0], list2[i][1]) in list2[:i] + list2[i + 1:j] + list2[j + 1:]:
                set1.add(''.join(sorted(list1[i] + list1[list2.index((list2[i][0], list2[j][1]))] + list1[list2.index((list2[j][0], list2[i][1]))] + list1[j])))
    print(set1)
    #list1 = list(dict_of_points.keys())
    #list2 = []
    #list3 = []
    #for i in range(len(list1)):
        #for j in range(i + 1, len(list1)):
            #if dict_of_points[list1[j]][1] == dict_of_points[list1[i]][1]:
                #list2.append((list1[i], list1[j]))
    #for i in range(len(list1)):
        #for j in range(i + 1, len(list1)):
            #if dict_of_points[list1[j]][0] == dict_of_points[list1[i]][0]:
                #list3.append((list1[i], list1[j]))
    #print(list2, list3)
    #set1 = set()
    #for i in range(len(list2)):
        #for j in range(i, len(list2)):
            #if i != j:
                #set1.add(list2[i] + list2[j])
    #print(set1)


get_count_of_rectangles(dict_of_points)