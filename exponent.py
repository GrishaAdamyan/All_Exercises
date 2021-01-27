#a = int(input())
#n = int(input())
#def ex(a,n):
    #if n == 1:
        #return a
    #elif n == 0 or a == 1:
        #return 1
    #else:
        #return ex(a,n-1)*a
#print(ex(a,n))

#a = int(input())
#n = int(input())
#def ex(a,n):
    #if a < 0 or n < 1:
        #return 'Mutqagreq urish tiv.'
    #else:
        #ex = 1
        #for i in range(1,n+1,1):
            #ex = ex * a
        #return ex
#print(ex(a,n))

#a = int(input())
#n = int(input())
#def ex(a,n):
    #if a < 0 or n < 1:
        #return 'Mutqagreq urish tiv.'
    #else:
        #ex = 1
        #i = 1
        #while i < n + 1:
            #ex = ex * a
            #i = i + 1
        #return ex
#print(ex(a,n))

a = int(input())
n = int(input())
def ex(a,n):
    if a < 0:
        return 'Mutqagreq urish tiv.'
    else:
        ex = 1
        while n > 0:
            ex = ex * a
            n = n - 1
        return ex
print(ex(a,n))