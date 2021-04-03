def sumOfTwo(a, b, v):
    a = set(a)
    return any(v - el in a for el in b)