list1 = [int(el) for el in input().split()]
list2 = [int(elem) for elem in input().split()]
my_set = set(list1) & set(list2)
if len(my_set) == 0:
    print('EMPTY')
else:
    list3 = []
    for el in my_set:
        list3.append(el)
    list3.sort()
    for el in list3:
        print(el)




#10 23 31
#5  10 49 31

#10
#31



#1 2 3
#10 20 30 40

#EMPTY



#5 9 7
#10 5 4 7 9

#5
#7
#9
