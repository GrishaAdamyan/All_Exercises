#n = int(input())
#def p(n):
    #if n < 2:
        #return 'Mutqagreq urish tiv.'
    #else:
        #for i in range(2,n,1):
            #if n % i == 0:
                #return 'No'
        #else:
            #return 'Yes'
#print(p(n))

#n = int(input())
#def p(n):
    #if n < 2:
        #return 'Mutqagreq urish tiv.'
    #else:
        #for i in range(2,n//2,1):
            #if n % i == 0:
                #return 'No'
        #else:
            #return 'Yes'
#print(p(n))

#n = int(input())
#def p(n):
    #if n < 2:
        #return 'Mutqagreq urish tiv.'
    #else:
        #for i in range(2,int(n**0.5)+1,1):
            #if n % i == 0:
                #return 'No'
        #else:
            #return 'Yes'
#print(p(n))

#n = int(input())
#import math
#def p(n):
    #if n < 2:
        #return 'Mutqagreq urish tiv.'
    #else:
        #for i in range(2,int(math.sqrt(n))+1,1):
            #if n % i == 0:
                #return 'No'
        #else:
            #return 'Yes'
#print(p(n))

#n = int(input())
#def p(n):
    #if n < 2:
        #print('Mutqagreq urish tiv')
    #else:
        #for i in range(2, n + 1):
            #for j in range(2, i):
                #if i % j == 0:
                    #break
            #else:
                #print(i)
#p(n)

n = int(input())
def p(n):
    if n < 2:
        print('Mutqagreq urish tiv')
    else:
        for i in range(2, n + 1):
            for j in range(2,int(i**0.5)+1,1):
                if i % j == 0:
                    break
            else:
                print(i)
p(n)