text = input().upper().split()
text1 = ['-'.join(list(word)) for word in text]
print(' '.join(text1))