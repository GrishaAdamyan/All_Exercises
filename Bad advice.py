n = int(input())
for i in range(n):
    advice = input()
    if advice[0:5] == 'Dont ' or advice[0:5] == 'dont ':
        print(advice[6:])
    else:
        print(advice)