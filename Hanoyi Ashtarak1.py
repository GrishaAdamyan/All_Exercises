n = int(input())
i = int(input())
j = int(input())
def h(n, i, j):
    if n > 0:
        h(n-1, i, 6-i-j)
        print(i, j, sep='-', end='; ')
        h(n-1, 6-i-j, j)
h(n, i, j)