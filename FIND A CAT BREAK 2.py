cat = -1
text = ''
count = 1
while text != 'STOP':
    text = input()
    if ('Cat' in text or 'cat' in text):
        cat = count
        break
    count += 1
print(cat)