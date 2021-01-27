a = [27, 25, 20, 17, 16, 10, 5, 3, 2]
def ex_min(a):
    return a.pop()
print(ex_min(a), a)

n = int(input())
def insert(n):
    a.append(n)
    i = len(a) - 1
    while i > 0 and a[i] > a[i - 1]:
        a[i], a[i - 1] = a[i - 1], a[i]
        i = i - 1
    return a
print(insert(n))

n = int(input())
def insert(n):
    a.append(n)
    for i in range(len(a)-1, 0, -1):
        if a[i] > a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
    return a
print(insert(n))