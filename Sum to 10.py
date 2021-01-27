summ = 0
count = 0
n = int(input())
while n != 0:
    summ += n
    count += 1
    if summ == 10:
        break
    n = int(input())
print(count)