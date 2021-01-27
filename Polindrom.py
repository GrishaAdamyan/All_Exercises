print('Պալինդրոմների մուտքագրման մարզասարք')
while True:
    print('Մուտքագրեք պալինդրոմ թիվ')
    number = n = int(input())
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + n % 10
        n //= 10
    if number == reverse:
        print('Դուք մուտքագրել եք պալինդրոմ: Ծրագրի աշխատանքը դադարեցվել է:')
        break
    print('Մուտքագրված թիվը պալինդրոմ չէ: Փորձեք կրկին:')