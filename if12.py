city1 = input()
city2 = input()
if city1 == 'Tula' and city2 != 'Penza' and city2 != 'Tula':
    print('YES')
elif city1 != 'Tula' and city1 != 'Penza' and city2 == 'Penza':
    print('YES')    
else:
    print('NO')