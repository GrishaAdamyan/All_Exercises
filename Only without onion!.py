#n = int(input())
#list1 = []
#for i in range(n):
    #list1.append(input())
#for j in range(len(list1)):
    #if not 'onion' in list1[j]:
        #print(list1[j],end=', ')


#list1 = [input() for i in range(int(input()))]
#for elem in list1:
    #if not 'onion' in elem:
        #print(elem,end=', ')

list1 = [input() for i in range(int(input()))]
print(', '.join(list1[j] for j in range(len(list1)) if not 'onion' in list1[j]))

#5
#onion 1
#potato 6
#peal the potato
#cut the onion
#fry everything
#potato 6, peal the potato, fry everything

