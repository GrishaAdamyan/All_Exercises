n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
k = int(input())
m = int(input())
for i in range(m):
    del list1[k-1::k]
for elem in list1:
    print(elem)


#7
#Mark
#Valeriy
#Akakiy
#Antonin
#Innokentiy
#Ippolit
#Julius
#3
#1
#Mark
#Valeriy
#Antonin
#Innokentiy
#Ippolit
#Julius