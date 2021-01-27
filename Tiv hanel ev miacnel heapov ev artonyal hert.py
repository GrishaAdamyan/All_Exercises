b = [5, 10, 7]
k = int(input())
def insert():
    b.append(k)
    j = len(b) - 1
    while j > 0 and b[j] < b[(j-1) // 2]:
        b[j], b[(j - 1) // 2], = b[(j - 1) // 2], b[j]
        j = (j - 1) // 2
    return b
print(insert())

def ex_min(b):
    b[0], b[len(b) - 1] = b[len(b) - 1], b[0]
    print(b.pop(), b)
    n = 0
    while 2*n+1 < len(b):
        min = n
        if b[min] > b[2*n+1]:
            min = 2*n+1
        if 2*n+2 < len(b) and b[min] > b[2*n+2]:
            min = 2*n+2
        if min == n:
            break
        else:
            b[n], b[min] = b[min], b[n]
        n = min
    print(a)
ex_min(b)

def pr(b):
    insert()
    ex_min(b)
pr(b)