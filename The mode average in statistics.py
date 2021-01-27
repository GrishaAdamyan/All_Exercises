text = input().split()
list1 = [int(n) for n in text]
list1.sort()
mijnativ = list1[len(list1)//2]
print(mijnativ, end=' ')
list2 = [text.count(letter) for letter in text]
for i in range(len(list1)):
    if list1.count(list1[i]) == max(list2):
        print(list1[i])
        break

#6 2 5 4 3 6 6
#5 6