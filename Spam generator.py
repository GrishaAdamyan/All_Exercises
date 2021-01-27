def profile(email, name, date, place = 'Gyumri'):
    print('To: {}'.format(email))
    print('Hello, {}!'.format(name))
    print('We would be happy to see you at the meeting beginning programmers in {}, which will be held {}.'.format(place, date))


profile('Gmail', 'Anun', '19:00', 'Yerevan')