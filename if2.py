print('Mutqagrel login')
login = input()
print('Mutqagrel pahestayin hasce')
pahestayin_hasce = input()
if '@' not in login and '@' in pahestayin_hasce:
    print('OK')
elif '@' in login and '@' in pahestayin_hasce:
    print('Invalid login')
elif '@' not in pahestayin_hasce and '@' not in login:
    print('Invalid address')
else:
    print('Invalid login')
    print('Invalid address')