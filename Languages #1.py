m = int(input())
n = int(input())
my_set = set()
m_set = set()
for i in range(m):
    new_elem = input()
    my_set.add(new_elem)
for j in range(n):
    elem = input()
    m_set.add(elem)
symm_diff = my_set ^ m_set
if len(symm_diff) > 0:
    print(len(symm_diff))
else:
    print('NO')
#3
#2
#Ivanov
#Petrov
#Vasechkin
#Ivanov
#Mikhailov