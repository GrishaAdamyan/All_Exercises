word = input()
short = word
long = ''
while word != 'stop':
    if len(word)>len(long):
        long = word
    elif len(word)<len(short):
        short = word
    word = input()
if set(short) <= set(long):
    print('YES')
else:
    print('NO')