# 1
#def string_for_1_to_n_number(n):
    #str1 = ''
    #for i in range(1, n + 1):
        #str1 += str(i)
    #return str1


#print(string_for_1_to_n_number(13))

def string_for_1_to_n_number(n):
    str1 = 1
    summ = 10
    for i in range(2, n + 1):
        if i < summ:
            pass
        else:
            summ *= 10
        str1 *= summ
        str1 += i
    return str1
    
print(string_for_1_to_n_number(100))