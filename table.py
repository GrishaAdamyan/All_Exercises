row = int(input())
col = int(input())
table = []
for _ in range(row):
    n = [el for el in input().split()]
    table.append(n)
for i in range(row):
    for j in range(col):
        print(table[i][j], end = '\t')
    print()
