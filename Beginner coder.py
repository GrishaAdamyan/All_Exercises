text = input()
for i in range(len(text)-1):
    print(ord(text[i]), end=', ')
print(ord(text[-1]))