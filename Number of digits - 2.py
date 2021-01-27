def num_digits(number):
    count = 1
    while number > 9:
        number //= 10
        count += 1
    return count


print(num_digits(1655))