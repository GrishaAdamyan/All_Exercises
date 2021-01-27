def who_are_you_and_hello():
    name = input()
    if name == name[0].upper()+name[1:].lower() and name.isalpha():
        print('Hello,', name + '!')
    else:
        who_are_you_and_hello()


who_are_you_and_hello()

def who_are_you_and_hello():
    name = input()
    while name != name[0].upper()+name[1:].lower() and name.isalpha():
        name = input()
    print('Hello,', name + '!')


who_are_you_and_hello()
#Why do you need to know that?
#All right
#Harry Potter
#Harry 1
#Harry1
#Harry!
#HARRY
#Harry
#Hello to you
#Ron?
#Ron

#Hello, Harry!