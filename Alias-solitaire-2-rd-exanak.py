qanak = int(input())
while qanak > 0:
    hanvox_tiv = int(input())
    if 1 <= hanvox_tiv <= 3 and hanvox_tiv <= qanak:
        qanak -= hanvox_tiv
    print(qanak)
input()