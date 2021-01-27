# 1
def buildPalindrome(string):
    if string == string[::-1]: # henc skzbic stugum enq polindrom e te che
        return string
    i = 0
    while string[i:] != string[i:][::-1]: # stugum enq te vortexic minchev verj e gtnvum stringi substring polindrom@
        i += 1
    return string + string[i - 1::-1] # entarkum enq konkatenaciayi string@ ev stringi ayn mas@ vor@ chi nerarum substring polindrom@


print(buildPalindrome('abaa'))

# 2
#set1 = set()
#def all_increasing_sequences(k, n, a = 1, b = 2, c = 3):
    #cort1 = (a, b, c)
    #if a <= n and b <= n and c <= n:
        #set1.add(cort1)
    #if c >= n and b == c - 1 and a == c - 2:
        #return set1
    #elif c >= n and b >= c - 1:
        #return all_increasing_sequences(k, n, a + 1, a + 2, a + 3)
    #elif c >= n:
        #return all_increasing_sequences(k, n, a, b + 1, b + 2)
    #return all_increasing_sequences(k, n, a, b, c + 1)


#print(all_increasing_sequences(3, 10))


#set1 = set()
#def all_increasing_sequences(k, n):
    #list1 = []
    #for i in range(1, k + 1):
        #list1.append(i)
    #tup1 = tuple(list1)
    #count = 0
    #for i in range(len(tup1)):
        #if tup1[i] <= n:
            #count += 1
    #if count == len(tup1):
        #set1.add(tup1)
    #else:
        #if c >= n and b == c - 1 and a == c - 2:
            #return set1
        #elif c >= n and b >= c - 1:
            #return all_increasing_sequences(k, n, a + 1, a + 2, a + 3)
        #elif c >= n:
            #return all_increasing_sequences(k, n, a, b + 1, b + 2)
    #return all_increasing_sequences(k, n, a, b, c + 1)


#print(all_increasing_sequences(3, 4))