# 1
def step_count(a):
    count = 0
    for i in range(0, len(a)-1, 1):
        if a[i] >= a[i+1]:
            count += (a[i] - a[i+1]) + 1
            a[i+1] = a[i+1] + (a[i] - a[i+1]) + 1
    return count


print(step_count([1, 1, 1]))

# 2
def check(list_1):
    list_1.insert(0,min(list_1)-1)
    count=0
    for i in range(2,len(list_1)):
        if list_1[i]<=list_1[i-1] and list_1[i]>list_1[i-2]:
            count+=1
            list_1[i-1]=list_1[i]
        elif list_1[i]<=list_1[i-1] and list_1[i]<=list_1[i-2]:
            count+=1
            list_1[i]=list_1[i-1]
    return count<=1


print(check([1, 2, 1, 2]))