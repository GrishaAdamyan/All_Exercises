total = 0
print('Մուտքագրեք գները, ավարտելու համար մուտքագրեք -1:')
price = float(input())
while price > 0:
    if price > 1000:
        price = price - (price / 20)
    total = total + price  
    price = float(input())
print('Ընդհանուր արժեքը հավասար է', total)