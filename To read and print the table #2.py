row = int(input())
col = int(input())
table = [[input() for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        print(table[i][j], end = '\t')
    print()
print()
for i in range(col):
    for j in range(row):
        print(table[j][i], end = '\t')
    print()


#3
#2
#three
#clubs
#seven
#hearts
#queen
#spade

#three	clubs
#seven	hearts
#queen	spade

#three	seven	queen
#clubs	hearts	spade