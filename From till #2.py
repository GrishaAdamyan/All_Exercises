#list1 = input().split()
#for i in range(len(list1)):
    #list1[i] = int(list1[i])
#m = int(input())
#k = int(input())
#print(sum(list1[m:k+1]))

list1 = [int(n) for n in input().split()]
m, k = [int(num) for num in input().split()]
print(sum(list1[m:k+1]))

#9 4 8 100 8000 444
#2 4
#8108