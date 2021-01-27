a = [12,3,18,30,11,7,3,9,]
q = 0
for i in range(0, len(a), 1):
    if a[i] % 2 == 1:
        q = q + a[i]
if q < len(a)-q:
    print('len(a)-q')
if q == len(a)-q:
    print('q = len(a)-q')
if q > len(a)-q:
    print('q')  