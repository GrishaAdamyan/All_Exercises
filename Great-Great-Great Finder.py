n = int(input())
list = []
for i in range(n):
    list.append(input())
pntrvox = input()
for elem in list:
    if pntrvox in elem:
        print(elem)