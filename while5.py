a = [12,3,18,30,11,15,3,9]
min = a[0]
for i in range(1,len(a),1):
    if a[i] < min:
        min = a[i]
print(min)