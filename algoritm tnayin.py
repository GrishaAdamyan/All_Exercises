n = int(input())
def f(n):
    gumar = 0
    f = 1
    for i in range(1, n + 1):
        f *= i
        gumar += f
    return gumar


print(f(n))



n = int(input())
def f(n):
    f = 1
    print(0,'!=',1,sep='')
    for i in range(1, n + 1):
        f = f * i
        print(i,'!=',f,sep='')


f(n)