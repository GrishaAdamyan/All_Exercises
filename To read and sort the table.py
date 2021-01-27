#row = int(input())
#col = int(input())
#table = [[input() for j in range(col)] for i in range(row)]
#for i in range(len(table)):
    #if i == 0 or i == len(table)-1:
        #print('\t'.join(table[i]))
    #else:
        #for k in range(len(table[i]) - 1):
            #for j in range(len(table[i]) - 1 - k):
                #if table[i][j] > table[i][j + 1]:
                    #table[i][j], table[i][j + 1] = table[i][j + 1], table[i][j]
        #print('\t'.join(table[i]))

row = int(input())
col = int(input())
table = [[input() for j in range(col)] for i in range(row)]
for i in range(len(table)):
    if i == 0 or i == len(table)-1:
        print('\t'.join(table[i]))
    else:
        table[i].sort()
        print('\t'.join(table[i]))
        
        
        
#4
#3
#amazing
#three
#club
#happy
#seven
#worms
#desirable
#ace
#peak
#sinister
#lady
#peak

#amazing    three    club
#happy    seven    worms
#ace    desirable    peak
#sinister    lady    peak
