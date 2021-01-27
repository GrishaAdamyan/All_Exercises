cat = 0
flag = False
text = input()
count = 1
while text != 'STOP':
    if ('Cat' in text or 'cat' in text) and not flag:
        cat = count
        flag = True
    text = input()
    count += 1
if flag:
    print(cat)
else:
    print(-1)