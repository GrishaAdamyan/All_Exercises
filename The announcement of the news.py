n = int(input())
m = int(input())
for i in range(m):
    text = input()
    if len(text)<=n:
        print(text)
    else:
        print(text[:n-3], end='...''\n')

#25
#3
#The annual summit on global warming has began
#New Year is coming!
#Python and Javascript are two of the most popular programming languages.
#The annual summit on g...
#New Year is coming!
#Python and Javascript ...