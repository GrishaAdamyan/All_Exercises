# 1
#text = input()
#sent = ""
#sent = sent.join(text[text.index(letter)] for letter in text if text[text.index(letter)].isalpha() or text[text.index(letter)] == ' ')
#print(sent)

#text = input()
#text_2 = ''
#for i in text:
#    if i.isalnum() or i == ' ':
#        text_2 += i
#    else:
#        text_2 += ' '
#print(text_2)

# 2
#number = input()
#a = 0
#for i in range(len(number)):
    #a += int(number[i])
#print(f"{a / (i+1):.1f}")

#list_2 = [int(el) for el in input()]
#print(round(sum(list_2) / len(list_2), 1))

# 3
#text = input().split()
#count = 0
#for word in text:
    #if word[0].isupper():
        #count += 1
#print(count)

# 4
#variable = input()
#print('True' if variable[0].isalpha() and variable[1:].isalnum() or variable[0].isalpha() and variable[1:].isalnum() and '_' in variable else 'False')

#text = input().replace('_','')
#print(text.isalnum() and text[0].isalpha())