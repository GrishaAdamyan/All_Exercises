n = int(input())
x = 'Eurasia'
y = 'Eastasia'
for i in range(n):
    text = input()
    if text == 'Who is the enemy?':
        print(x)
    if text == 'Who is a friend?':
        print(y)
    if text == 'Change':
        x, y = y, x