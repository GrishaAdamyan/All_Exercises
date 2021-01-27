#str1 = input()
#list1 = str1.split()
#for elem in list1:
    #print(int(elem) * '*')

print('\n'.join([int(elem)* '*' for elem in input().split()]))