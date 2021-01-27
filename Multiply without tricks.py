qanak = 0
k = 1
while qanak < 6:
    n = int(input())    
    if n > 0 or n < 0:
        k = k * n
        qanak += 1
    else:
        qanak += 1
print(k)