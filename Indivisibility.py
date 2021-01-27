#text = input().lower()
#list1 = []
#for i in range(len(text)):
    #list1.append(text.count(text[i]))
#print(max(list1))

text = input().lower()
list1 = [text.count(letter) for letter in text]
print(max(list1))

#Indivisibility
#6