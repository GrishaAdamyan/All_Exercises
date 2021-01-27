# Ex 1
#text = input().lower().split(';')
#count = 0
#for i in range(len(text)):
    #if 'a' in text[i] or 'b' in text[i] or 'c' in text[i]:
        #count += 1
#print(count)

# Ex 2
#list1 = [int(x) for x in input().split()]
#n, k = [int(num) for num in input().split()]
#count = 0
#for i in range(len(list1)):
    #if list1[i] % n == k:
        #count += list1[i]
#print(count)

# Ex 3
#text = input()
#dictionary = {}
#for i in range(len(text)):
    #if text[i] not in dictionary and text[i] == text[0] or text[i] == text[text.find(' ')+1] or text[i] == text[text.rfind(' ')+1]:
        #dictionary[text[i]] = 1
    #elif text[i] in dictionary and text[i] == text[0] or text[i] == text[text.find(' ')+1] or text[i] == text[text.rfind(' ')+1]:
        #dictionary[text[i]] += 1
    #elif text[i] == ' ':
        #continue
    #else:
        #dictionary[text[i]] = 0
#print(dictionary)