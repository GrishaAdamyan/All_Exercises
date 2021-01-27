m = int(input())
my_set = set()
m_set = set()
while m:
    n = int(input())
    for i in range(n):
        elem = input()
        my_set.add(elem)
        if m_set == set():
            m_set = my_set
        m_set = m_set & my_set
        my_set.clear()
        m -= 1
for elem in m_set:
    print(elem)

#2
#4
#Alexandrova
#Borisova
#Vasiliev
#Ivanov
#2
#Vasiliev
#Alexandrova

#Alexandrova
#Vasiliev

#3
#4
#Alexandrova
#Borisov
#Vasiliev
#Ivanov
#4
#Petrov
#Borisov
#Vasiliev
#Alexandrova
#4
#Ivanov
#Alexandrova
#Petrov
#Borisov

#Alexandrova
#Borisov