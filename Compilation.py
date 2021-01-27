nums = [int(n) for n in input().split()]
text = input().lower().split()
new_text = []
for t in nums:
    new_text.append(text[t - 1])
new_text[0] = new_text[0][0].upper() + new_text[0][1:]
#new_text[0] = new_text[0].capitalize()
print(' '.join(new_text))