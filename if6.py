b = int(input())
c = int(input())
a = b / c
if a < 1/1000000:
    print(1000000)
else:
    print(c / b)