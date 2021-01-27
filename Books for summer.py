m = int(input())
n = int(input())
m_set = set()
for i in range(m):
    new_elem = input()
    m_set.add(new_elem)
for j in range(n):
    elem = input()
    if elem in m_set:
        print('YES')
    else:
        print('NO')

#4
#2
#Hobbit
#Alice in Wonderland
#Tom Soyer
#Treasure island
#Tom Soyer
#Lord of the Rings	
#YES
#NO
#4
#4
#Hobbit
#Alice in Wonderland
#Tom Sawyer
#Treasure island
#Buratino
#Hobbit
#Treasure island
#War and peace    
#NO
#YES
#YES
#NO