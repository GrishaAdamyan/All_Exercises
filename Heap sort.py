#a = [10,5,3,15,9,12,7,5,17,2]
#def hs(a):
    #for i in range(1,len(a),1):
        #j = i
        #while j > 0 and a[j] < a[(j-1)//2]:
            #a[j],a[(j-1)//2]=a[(j-1)//2],a[j]
            #j = (j-1)//2
    #for k in range(0,len(a)-1,1):
        #a[0],a[len(a)-1-k]=a[len(a)-1-k],a[0]
        #n=0
        #while 2*n+1 < len(a)-1-k:
            #min = n
            #if a[min] > a[2*n+1]:
                #min = 2*n+1
            #if 2*n+2 < len(a)-1-k and a[min] > a[2*n+2]:
                #min = 2*n+2
            #if min == n:
                #break
            #else:
                #a[min],a[n] = a[n],a[min]
                #n = min
    #return a 
#print(hs(a))



#a = [10,5,3,15,9,12,7,5,17,2]
#def hs(a):
    #for i in range(1,len(a),1):
        #j = i
        #while j > 0 and a[j] > a[(j-1)//2]:
            #a[j],a[(j-1)//2]=a[(j-1)//2],a[j]
            #j = (j-1)//2
    #for k in range(0,len(a)-1,1):
        #a[0],a[len(a)-1-k]=a[len(a)-1-k],a[0]
        #n=0
        #while 2*n+1 < len(a)-1-k:
            #max = n
            #if a[max] < a[2*n+1]:
                #max = 2*n+1
            #if 2*n+2 < len(a)-1-k and a[max] < a[2*n+2]:
                #max = 2*n+2
            #if max == n:
                #break
            #else:
                #a[max],a[n] = a[n],a[max]
                #n = max
    #return a 
#print(hs(a))



a = [10,5,3,15,9,12,7,5,17,2]
def hs(a):
    for i in range(1,len(a),1):
        j = i
        while j > 0 and a[j] < a[(j-1)//2]:
            a[j],a[(j-1)//2]=a[(j-1)//2],a[j]
            j = (j-1)//2
    for k in range(0,len(a)-1,1):
        a[0],a[len(a)-1]=a[len(a)-1],a[0]
        print(a.pop())
        n=0
        while 2*n+1 < len(a):
            min = n
            if a[min] > a[2*n+1]:
                min = 2*n+1
            if 2*n+2 < len(a) and a[min] > a[2*n+2]:
                min = 2*n+2
            if min == n:
                break
            else:
                a[min],a[n] = a[n],a[min]
                n = min
    return a.pop()
print(hs(a))