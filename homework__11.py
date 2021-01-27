# 1
def length_of_number(n):
    count = 1
    product = 10
    if 0 < n < 10:
        return count
    while n // product >= 10:
        n //= product
        count += 1
    return count + 1


print(length_of_number(999))

# 2
def function(list1, k):
    t = 1
    set1 = set()
    start, end = 0, 0 + t
    while start <= len(list1) - 1:
        if list1[start] + list1[end] == k:
            set1.add((list1[start], list1[end]))
        end += 1
        if end == len(list1):
            end = t
            t += 1
            start += 1
    for elem in set1:
        print(elem)

function([5, 2, 4, 4, 3], k = 8)