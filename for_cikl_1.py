a = [12,5,3,10,3,7,9]
k = int(input())
for i in range (0,len(a),1):
    if a[i] == k:
        print('yes')
        break
else:
    print('no')