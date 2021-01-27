a = int(input())
b = int(input())
def Нод(a,b):
    while b != 0:
        a,b = b,a%b
    return a
print(Нод(a,b))