n = int(input())
list1 = []
for i in range(n):
  title = ''
  text = input()
  while text != '*':
    title += text + ' '
    text = input()
  list1.append('-'.join(title.split()))
print(', '.join(list1[::-1]))

#3
#Just
#nice guy
#*
#Most
#Productive
  #The grower
#Bobs'
#*
#Jack
#The Winner Of The Giants
#*
#Jack-The-Winner-Of-The-Giants, Most-Productive-The-grower-Bobs', Just-nice-guy