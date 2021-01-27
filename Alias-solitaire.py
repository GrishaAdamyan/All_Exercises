qanak = int(input())
while qanak > 0:
    hanvox_tiv = int(input())
    if hanvox_tiv > 3:    
        print(qanak)
    elif 1 <= hanvox_tiv <= 3 and qanak - hanvox_tiv >= 0:
        qanak -= hanvox_tiv
        print(qanak)
    else:
        print(qanak)
        
#1
#1
#5
#3
#2
#4
#4
#3