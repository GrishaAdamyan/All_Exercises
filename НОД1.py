a = int(input())
b = int(input())
def e(a,b):
    if b != 0:
        print(a,b)
        return e(b,a%b)
    else:
        print(a,b)
        return a
print(e(a,b))