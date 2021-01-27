#list1 = [str(i ** 2) for i in range(int(input()))]
#print(' '.join(list1))

print(' '.join(str(i ** 2) for i in range(int(input()))))