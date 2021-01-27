def print_long_words(text):
    text = text.lower().split()
    for elem in text:
        count = 0
        for el in elem:
            if el in 'aeiouy':
                count += 1
        if count >= 4:
            for element in elem:
                if element.isalpha():
                    print(element, end='')
            print()


print_long_words('In the middle of difficulty lies opportunity."')

#print_long_words('In the middle of difficulty lies opportunity."')
#difficulty
#opportunity