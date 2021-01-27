def take_large_banknotes(banknotes):
    list1 = []
    for elem in banknotes:
        if elem > 10:
            list1.append(elem)
    return list1


print(*take_large_banknotes([100]))

def take_large_banknotes(banknotes):
    list1 = [elem for elem in banknotes if elem > 10]
    return list1


print(*take_large_banknotes([100]))