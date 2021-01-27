n = int(input())
dictionary = {}
for i in range(n):
    text = input()
    dictionary[text[:text.find(' ')]] = text[text.find(' ')+1:]
    #text = input().split()
    #dictionary[text[0]] = ' '.join(text[1:])
m = int(input())
for j in range(m):
    word = input()
    print(dictionary.get(word,'Not in the dictionary'))


#3
#Example An item of information that is typical of a class or group
#Task Any piece of work that is undertaken or attempted
#Study applying the mind to learning and understanding a subject
#4
#Example
#Word
#Task
#Example

#An item of information that is typical of a class or group
#Not in the dictionary
#Any piece of work that is undertaken or attempted
#An item of information that is typical of a class or group
