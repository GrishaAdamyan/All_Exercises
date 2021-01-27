n = int(input())
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