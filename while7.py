a = [12,3,18,30,11,7,3,9,]
q = 0
c = 0
for i in range(0, len(a), 1):
    if a[i] % 2 == 1:
        q = q + a[i]
    if a[i] % 2 == 0:
        c = c + a[i]
if q < c:
    print('c')
if q == c:
    print('q = c')
if q > c:
    print('q')