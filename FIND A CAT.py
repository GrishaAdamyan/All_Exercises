n = int(input())
find = False
for i in range(n):
    text = input()
    if 'Cat' in text or 'cat' in text:
        find = True
if find:
    print('Meow')
else:
    print('NO')