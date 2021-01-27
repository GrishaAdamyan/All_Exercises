# 1
for i in range(1,101):
    for j in range(1,101):
        if i ** j == j ** i and i != j != i ** j:
            print(i,'-',j)
            print()

# 2
for i in range(1,51):
    for j in range(1,i+1):
        print(i,end=' ')
    print()