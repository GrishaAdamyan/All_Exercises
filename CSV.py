r = int(input())
table = [input().split(',') for i in range(r)]
n = int(input())
for j in range(n):
    x, y = [int(z) for z in input().split(',')]
    print(table[x][y])

#4
#Once,upon a time
#there, was, a
#small, village, near
#the blue see,,
#4
#0,0
#1,2
#3,1
#3,0
#Once
 #a

#the blue see