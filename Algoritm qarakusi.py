#row = col = 6
#for i in range(row):
    #for j in range(col):
        #if i == 0 or i == row - 1 or j == 0 or j == col - 1:
            #print('*', end = '  ')
        #else:
            #print(' ', end = '  ')
    #print()
#print()
#row = col = 6
#for i in range(row):
    #for j in range(col):
        #print('*', end='  ')
    #print()

for i in range(6):
    if i == 0 or i == 5:
        print(6 * '* ')
    else:
        print('*         *')