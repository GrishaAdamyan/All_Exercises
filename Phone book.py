n = int(input())
list1 = [el for _ in range(n) for el in input().split()]
dictionary = {}
for i in range(1,len(list1),2):
    if list1[i] not in dictionary:
        dictionary[list1[i]] = list1[i-1]
    else:
        dictionary[list1[i]] += ' ' + list1[i-1]
m = int(input())
for _ in range(m):
    print(dictionary.get(input(),'Not in the phone book'))


#3
#3129102 Vanya
#79007619273 Kolya
#79120123456 Vanya
#3
#Kolya
#Vanya
#Oleg

#79007619273
#3129102 79120123456
#Not in the phone book