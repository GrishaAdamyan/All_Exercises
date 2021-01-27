a = int(input())
b = int(input())
def нод(a,b):
    while b != 0:
        a,b = b,a%b
    return a
def нок(a,b):
    return int((a*b)/нод(a,b))
print(нок(a,b))