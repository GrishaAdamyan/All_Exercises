list1 = ['cabbage soup','borscht','gazpacho','oatmeal soup','chicken soup']
n = int(input())
for i in range(n):
    print(list1[i % len(list1)])