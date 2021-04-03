n = int(input())
list = []
for i in range(n):
    list.append(input())
m = int(input())
for elem in list:
    if len(elem) >= m:
        print(elem[m-1],end='')