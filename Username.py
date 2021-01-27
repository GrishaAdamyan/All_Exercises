username = input()
right = True
for i in range(len(username)):
    if username[i] not in '1234567890_abcdefghijklmnopqrstuvwxyz':
        print('Invalid character:', username[i])
        right = False
        break
if right:
    print('OK')