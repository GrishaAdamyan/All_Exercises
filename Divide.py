n = int(input())
m = 0
for i in range(1,n+1,1):
    if n % i == 0:
        print(i, end=' ')
        m += 1
if m == 2:
    print('\nPRIME')
else:
    print('\nNO')