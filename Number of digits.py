def num_digits(number):
    str_number = str(number)
    return len(str_number)


print(num_digits(157))

def num_digits(number):
    str_number = str(number)
    count = 0
    for num in str_number:
        count += 1
    return count


print(num_digits(157))