text = input().upper()
for i in range(len(text)):
    if text[i] == ' ':
        print()
        continue
    print(MORSE[text[i]],end=' ')


#Help me SOS
#.... . .-.. .--.
#-- .
#... --- ...