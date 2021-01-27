a = [12,3,18,30,11,15,3,9]
q = 0
for i in range(0, len(a), 1):
    if a[i] % 15 == 0:
        q = q + 1
        print(a[i])
print(q)