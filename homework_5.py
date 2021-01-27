# 1
xmbak = input().split(', ')
xmbak1 = []
for i in range(len(xmbak)):
    xmbak1.append(xmbak[i].split(': '))
dict1 = {}
for i in range(len(xmbak1)):
    dict1[xmbak1[i][0]] = int(xmbak1[i][1])
list1 = []
for i in range(len(xmbak)):
    list1.append(input().split(', '))
xmbak2 = []
for i in range(len(xmbak1)):
    xmbak2.append([])
    xmbak2[i].append(xmbak1[i][0])
i = j = 0
dict2 = {}
while i < len(xmbak1) and j < len(xmbak1):
    if dict1[xmbak1[i][0]] != len(list1[j]):
        j += 1
    else:
        for k in range(len(list1[j])):
            if list1[j][k] in dict2:
                dict2[list1[j][k]] = dict2[list1[j][k]] + xmbak2[i]
            else:
                dict2[list1[j][k]] = xmbak2[i]
        i += 1
        j = 0
names = input().split(', ')
list2 = []
for i in range(len(names)):
    list2.append(len(dict2[names[i]]))
print(': '.join([names[list2.index(min(list2))]] + dict2[names[list2.index(min(list2))]]))

# 2
#check_number = 1
#list1 = []
#list2 = []
#def add_item(itemName, itemCost):
    #global list1
    #global list2
    #list1.append(itemName)
    #list2.append(itemCost)
    #return


#def print_receipt():
    #global check_number
    #if len(list1) == 0:
        #return
    #print('Check {}. Number of items: {}'.format(check_number, len(list1)))
    #for i in range(len(list1)):
        #print(list1[i], '-', list2[i])
    #print('Total:', sum(list2))
    #print('-----')
    #check_number += 1
    #list1.clear()
    #list2.clear()
    #return


#add_item('Keyboard', 100)
#print_receipt()

#add_item('Mouse', 70)
#print_receipt()
#print_receipt()

#add_item('Screen', 15)
#add_item('Screen', 15)
#add_item('Pen', 5)
#print_receipt()

#add_item('Screen', 15)
#add_item('Screen', 15)
# Cancel
#Robototexnika: 3, Yandex.Licey: 2
#Ivanov, Petrov
#Ivanov, Alekseev, Sidorov
#Ivanov, Petrov