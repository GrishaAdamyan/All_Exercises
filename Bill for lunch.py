count = 0
def count_food(days):
    global count
    for num in days:
        count += daily_food[num-1]
    return count


daily_food = [0, 150, 150]
print(count_food([2, 3]))