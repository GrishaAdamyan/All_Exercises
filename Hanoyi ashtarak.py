n = int(input())
i = int(input())
j = int(input())
def h(n, i, j):
    if n > 1:
        h(n-1, i, 6-i-j)
        print(i, j, sep='-', end='; ')
        h(n-1, 6-i-j, j)
    if n == 1:
        print(i, j, sep='-', end='; ')
h(n, i, j)