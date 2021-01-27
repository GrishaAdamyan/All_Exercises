hasak = input()
minn = 191
maxx = 149
astr = 0
while hasak != '!':
    h = int(hasak)
    if 190 >= h >= 150:
        astr += 1
        if h > maxx:
            maxx = h
        if h < minn:
            minn = h
    hasak = input()
print(astr)
print(minn, maxx)