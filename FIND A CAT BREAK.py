n = int(input())
flag = False
for i in range(n):
    text = input()
    if 'Cat' in text or 'cat' in text:
        flag = True
        break
if flag:
    print('Meow')
else:
    print('NO')