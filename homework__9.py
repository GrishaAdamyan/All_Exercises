# 1
#list1 = [2, 2, 2, 2, 2, 2, 1, 2]
#def nonreal(list1, i = 0):
    #k = 1
    #if (i + 2) < len(list1):
        #if sum(list1[k * i:k * (i + 2)]) == 6:
            #k += 1
            #return nonreal(list1, i + 3)
        #else:
            #return list1.index(1)
    #elif (i + 2) == len(list1):
        #if sum(list1[k * i:k * (i + 1)]) != 4:
            #return list1.index(1)
        #else:
            #return 'All real'


#print(nonreal(list1))

# 2
def pakagic(string, i = 0):
    list1 = list(string)
    if list1[i:].count('(') == 1:
        word = list1[i:][list1[i:].index('('):list1[i:].index(')') + 1]
        word = word[::-1]
        list1[list1.index(word[::-1])] = word
        new_str = ''
        for elem in list1:
            if elem == '(' or elem == ')':
                continue
            else:
                new_str += elem
        return new_str
    else:
        return pakagic(string, i = list1[i:].index('(') + 1)


print(pakagic('(bar)'))