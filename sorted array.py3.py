a = [5,3,20,12,9,7,5,18,2]
for i in range(-1,len(a)-2,1):
    for j in range(1,len(a)-1-i,1):
        if a[j-1]>a[j]:
            a[j-1],a[j]=a[j],a[j-1]
print(a)