n = int(input())
for j in range(1,n+1,1):
    for i in range(1,n,1):
        print(j * i, sep='', end='\t')
    print(n * j)