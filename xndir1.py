a = int(input())
k = 0
t = a
while a != 0:
   if a > t:
      t = a
      k = 0
   if a == t:
      k += 1
   a = int(input())
print(k)