n = int(input())
for i in range(1,n+1,1):  
    for j in range(1,n+1,1):
        print(i, ' * ', j, ' = ', i * j, sep='', end='\n')