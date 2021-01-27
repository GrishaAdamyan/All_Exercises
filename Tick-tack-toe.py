n = int(input())
list1 = [input() for i in range(n)]
flag = False
for i in range(n):
    if 'xxx' in list1[i]:
        print('x')
        flag = True
        break
    if 'ooo' in list1[i]:
        print('o')
        flag = True
        break
if flag == False:
    list2 = []
    for i in range(n):
        for j in range(n):
            list2.append(list1[j][i])
    for i in range(0,n*n,n):
        if 'xxx' in ''.join(list2[i:n]):
            print('x')
            flag = True
            break
        if 'ooo' in ''.join(list2[i:n]):
            print('o')
            flag = True
            break
if flag == False:
    print('-')

#4
#.o.x
#xx.o
#ooo.
#xxo.
#o