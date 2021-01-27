def matrixx(arg):
    if arg == 'matrix()':
        print(0)
    elif arg == 'matrix(n)':
        for i in range(n):
            for j in range(n):
                print(0)
    elif arg == 'matrix(n, m)':
        for i in range(m):
            for j in range(n):
                print(0)
    elif arg == 'matrix(n, m, a)':
        for i in range(m):
            for j in range(n):
                print(a)


matrixx('matrix(2)')