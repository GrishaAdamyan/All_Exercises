def ask_password():
    for i in range(3):
        text = input()
        if text == 'password':
            print('Password accepted')
            break
        if i == 2:
            print('Access denied')


ask_password()