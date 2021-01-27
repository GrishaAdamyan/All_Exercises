# 1
def exevni(n):
    k = 1
    m = 1
    while m <= n:
        for i in range(k):
            print(m, end=' ')
            m += 1
            if m > n:
                break
        k += 1
        print()
    print()


exevni(8)

# 2
m = 0
def isLucky(list1):
    for i in range(0, len(list1), 2):
        if list1[i] == i:
            if list1[i - 1] == i - 1:
                return i - 1
            return i
        elif list1[i] > i:
            if list1[i - 1] == i - 1:
                return i - 1            
    return -1


print(isLucky([0, 2]))