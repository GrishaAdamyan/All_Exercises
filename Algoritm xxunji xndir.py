#h = int(input())
#a = int(input())
#b = int(input())
#summ = 0
#orer = 0
#while summ < h:
    #summ += a
    #orer += 1
    #if summ < h:
        #summ -= b
#print(orer)

#h = int(input())
#a = int(input())
#b = int(input())
#k = (h-a) // (a-b)
#if (h-a)%(a-b) == 0:
    #print(k+1)
#else:
    #print(k+2)

import math
h = int(input())
a = int(input())
b = int(input())
print(math.ceil((h-a)/(a-b)+1))