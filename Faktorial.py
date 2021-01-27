#n = int(input())
#k = 1
#for i in range(2,n+1,1):
    #k = k * i
#print(k)

#n = int(input())
#k = 1
#i = 2
#while i<=n:
    #k = k * i
    #i = i + 1
#print(k)

#n = int(input())
#f = 1
#while n > 1:
    #f = f * n
    #n = n - 1
#print(f)

#n = int(input())
#k = 1
#print(0,'!=',1,sep='')
#for i in range(1,n+1,1):
    #k = k * i
    #print(i,'!=',k,sep='')


#summ = 0
#n = int(input())
#for i in range(1,n + 1):
    #k = 1
    #for j in range(1,i + 1):
        #k = j * k
    #summ = k + summ
#print(summ)


n = int(input())
f = 1
summ = 0
for i in range(1,n + 1,1):
    f = f * i
    summ = summ + f
print(summ)