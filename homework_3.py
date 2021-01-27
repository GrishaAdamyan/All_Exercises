# 1
n = int(input())
list1 = []
for i in range(n):
    name = input("name: ")
    mark = float(input("mark: "))
    list1.append([mark,name])
list1.sort()
low = [list1[j][0] for j in range(n)].count([list1[j][0] for j in range(n)][0])
i = low
while i <= len(list1)-1 and [list1[j][0] for j in range(n)][i] == [list1[j][0] for j in range(n)][low]:
    print(list1[i][1])
    i += 1

# 2
def describe_the_string(string):
    dict_ = {}
    for symbol in set(string):
        dict_[symbol] = string.count(symbol)
    return dict_


def dict_contains_dict(dict_1, dict_2): # dict_1 is greater than dict_2
    for key in dict_2:
        if dict_1.get(key, 0) < dict_2[key]:
            return False
    return True


def minimum_length_substring(superString, subString):
    super_length = len(superString)
    sub_length = len(subString)
    desc_of_subString = describe_the_string(subString)
    t = 0
    while sub_length + t <= super_length:
        start, end = 0, sub_length + t
        while end <= super_length and not dict_contains_dict(describe_the_string(superString[start:end]), desc_of_subString):
            start += 1
            end += 1
        if dict_contains_dict(describe_the_string(superString[start:end]), desc_of_subString):
            return superString[start:end]
        elif end > super_length:
            t += 1
    return "The superstring doesn't contain the substring"



superString = input('Input the superstring: ')
subString = input('Input the substring: ')
print(minimum_length_substring(superString, subString))