n = int(input())
list1 = []
for i in range(n):
    list1.append(int(input()))
m = int(input())
for j in range(n):
    k = m / list1[j]
    if k in list1:
        print('YES')
        break
else:
    print('NO')
#4
#37
#3
#99
#55
#111
#YES
