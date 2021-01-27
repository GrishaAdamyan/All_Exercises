# 1
word = input('Enter number ')
list1 = []
while word != 'End':
    list1.append(int(word))
    word = input('Enter number ')
dictionary = {}
for number in list1:
    dictionary[number] = dictionary.get(number, 0) + 1
print(dictionary)

# 2
string = input()
odd_symbols = 0
for symbol in set(string):
    if string.count(symbol) % 2 == 1:
        odd_symbols += 1
print(len(string) % 2 == odd_symbols)