import random

lowers_uppers_numbers_symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]{}()*;/,_-'
password = ''.join(random.sample(lowers_uppers_numbers_symbols, 16))
print(password)