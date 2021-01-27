def countBits(n):
    while n // 2 >= 1:
        countBits.count += 1
        n //= 2
    return countBits.count

countBits.count = 1

print(countBits(50))