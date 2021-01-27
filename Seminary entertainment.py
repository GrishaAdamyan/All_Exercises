num = int(input())
while num <= 1000000000:
    num *= int(str(num)[0])
    if str(num)[0] == '1':
        break
print(num)