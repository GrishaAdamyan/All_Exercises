print('Մուտքագրեք քարերի քանակը։')
qanak = int(input())
while qanak > 0:
    print('Հիմա հերթը համակարգչինն է։')    
    if qanak % 4 == 1:
        hanvox_tiv = 1
    if qanak % 4 == 2:
        hanvox_tiv = 2
    if qanak % 4 == 3:
        hanvox_tiv = 3
    if qanak % 4 == 0:
        hanvox_tiv = 1
    qanak -= hanvox_tiv
    print(qanak)
    if qanak == 0:
        print('Հաղթեց համակարգիչը։')
    else:
        print('Հիմա օգտատիրոջ հերթն է։')
        print('Կարելի է մուտքագրել 1 կամ 2 կամ 3։')
        hanvox_tiv = 0
        while not (1 <= hanvox_tiv <= 3 and qanak - hanvox_tiv >= 0):
            hanvox_tiv = int(input())
        qanak -= hanvox_tiv
        print(qanak)   
        if qanak == 0:
            print('Հաղթեց օգտատերը։')