import math
def discriminant(a, b, c):
    D = (b ** 2) - (4 * a * c)
    return D


print(discriminant(1, 2, 1))

def larger_root(p,q):
    return (- p + (math.sqrt(discriminant(1, p, q)))) / 2


print(larger_root(2, 1))

def smaller_root(p,q):
    return (- p - (math.sqrt(discriminant(1, p, q)))) / 2


print(smaller_root(2, 1))

def main(p, q):
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))


main(-2.5, 1)