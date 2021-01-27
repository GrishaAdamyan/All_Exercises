#list1 = (input().split())
#list2 = []
#for i in range(len(list1)):
    #list2.append(int(list1[i])**2)
#for elem in list2:
    #print(elem,end=' ')

#list1 = input().split()
#list2 = [int(list1[i])**2 for i in range(len(list1))]
#for elem in list2:
    #print(elem,end=' ')

list1 = input().split()
print(' '.join(str(int(list1[i])**2) for i in range(len(list1))))