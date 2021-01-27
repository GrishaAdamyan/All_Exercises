number = input()
odd = even = 0
for i in range(0, len(number), 2):
    odd += int(number[i])
for j in range(1, len(number), 2):
    even += int(number[j])
if odd == even:
    print('Երջանիկ է պիտերյան տարբերակով:')