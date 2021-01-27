a = [5,3,20,12,9,7,5,18,2]
for i in range(0,len(a)-1,1):
    for j in range(0,len(a)-1-i,1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)