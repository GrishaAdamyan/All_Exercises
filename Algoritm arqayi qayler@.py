a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a-c) > 1 or (c-a) > 1 and (b-d) > 1 or (d-b) > 1:
    print('NO')
else:
    print('YES')

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if -1 <= (a-c) <= 1 and -1 <= (b-d) <= 1:
    print('YES')
else:
    print('NO')

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a-c) <= 1 and abs(b-d) <= 1:
    print('YES')
else:
    print('NO')