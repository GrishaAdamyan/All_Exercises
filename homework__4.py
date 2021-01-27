# 1
#coordinates = [5,8,9,13,14]
#i = 0
#qayl = 2
#while i < len(coordinates):
    #if coordinates[i] % qayl == 0:
        #qayl += 1
        #i = 0
    #elif i == len(coordinates)-1 and coordinates[i] % qayl != 0:
        #print(qayl)
        #break
    #else:
        #i += 1

# 2
havasarum = input()
count_tiv = 0
count_x = 0
start = 0
i = 0
while i != havasarum.index('=') + 1:
    if havasarum[i] == '-' or havasarum[i] == '+' or havasarum[i] == '=':
        if 'x' in havasarum[start:i]:
            if len(havasarum[start:i]) == 1 or havasarum[start:i] == '+x' or havasarum[start:i] == '-x':
                count_x += 1
            else:
                count_x += int(havasarum[start:havasarum.find('x')])
        else:
            count_tiv -= int(havasarum[start:i])
        start = i
    i += 1
start = havasarum.index('=') + 1
i = start + 1
while i != len(havasarum):
    if havasarum[i] == '-' or havasarum[i] == '+' or i == len(havasarum)-1:
        if 'x' in havasarum[start:i]:
            if len(havasarum[start:i]) == 1 or len(havasarum[start:i]) == 2 and havasarum[i] == '+' or havasarum[i] == '-':
                count_x += 1
            else:
                count_x += int(havasarum[start:havasarum.find('x')])
        else:
            count_tiv += int(havasarum[start:i+1])
        start = i
    i += 1
print(count_tiv / count_x)