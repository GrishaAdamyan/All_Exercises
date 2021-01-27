row = int(input())
col = int(input())
table = [[input() for j in range(col)] for i in range(row)]
for i in range(row):
    for j in range(col):
        print(table[i][j], end = '\t')
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