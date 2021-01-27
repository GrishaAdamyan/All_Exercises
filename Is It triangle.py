def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('This is a triangle')
    else:
        print('This is not a triangle')


triangle(int(input()), int(input()), int(input()))