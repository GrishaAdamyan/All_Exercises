#n = int(input())
#m = 'ABCDEFGH'
#for i in range(n,0,-1):
    #for j in range(0,n):
        #print(m[j]+str(i),end=' ')
        #if j == n-1:
            #print()
            
n = int(input())
m = 'ABCDEFGHI'
for i in range(n,0,-1):
    for j in range(n-1):
        print(m[j]+str(i),end=' ')
    print(m[j+1]+str(i),end='\n')

#n = int(input())
#m = 'ABCDEFGH'
#if n == 1:
    #m = m[0]
#if n == 2:
    #m = m[0:2]
#if n == 3:
    #m = m[0:3]
#if n == 4:
    #m = m[0:4]
#if n == 5:
    #m = m[0:5]
#if n == 6:
    #m = m[0:6]
#if n == 7:
    #m = m[0:7]
#if n == 8:
    #m = m[0:8]
#for i in range(n,0,-1):
    #for j in range(0,n):
        #print(m[j]*(n//n)+str(i),end=' ')
        #if j == n-1:
            #print()