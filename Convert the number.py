number = int(input())
print(number)
a = number//100
b = (number-(a*100))//10
c = number%10
if (a+b)>(b+c):
    print((a+b),(b+c), sep='')
else:
    print((b+c),(a+b), sep='')