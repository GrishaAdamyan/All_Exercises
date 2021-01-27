old_f = 1
cur_f = 1
limit = int(input())
while old_f <= limit:
    print(old_f)
    new_f = old_f + cur_f
    old_f = cur_f
    cur_f = new_f