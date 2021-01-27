#k = int(input())
#count = 0
#for i in range(5, k+1, 5):
    #while i / 5 == i // 5:
        #count += 1
        #i = i / 5
#print(count)

k = int(input())
count = 0
i = 5
while i <= k:
    count = count + (k // i)
    i = i * 5
print(count)