n = int(input())
city_set = set()
for i in range(n):
    city_set.add(input())
new_city = input()
if new_city in city_set:
    print('TRY ANOTHER')
else:
    print('OK')