def print_document(pages):
    for text in pages:
        if text[:text.find(' ')] == 'Confidentially':
            print('Further materials are classified')
            return
        elif text == pages[len(pages)-1] and text[:text.find(' ')] != 'Confidentially':
            print(text)
            print('Printed without cuts')
        else:
            print(text)


print_document(["Empty conversation", "that is not interesting", "to anyone"])