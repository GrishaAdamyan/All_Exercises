def circle_length(radius):
    pi = 3.14159
    length = 2 * radius * pi
    return length


print(circle_length(5))

def circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

print(circle_area(10))

def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))


main()