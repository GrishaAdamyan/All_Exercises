qanak = int(input())
hanvox_tiv = int(input())
while qanak - hanvox_tiv > 0:
    qanak -= hanvox_tiv
    print(qanak)
    hanvox_tiv = int(input())
    if qanak - hanvox_tiv == 0:
        print(0)
20
1
1
5
3
2
4
4