rocets = int(input())
roc_num = 0
while roc_num < rocets:
    roc_num += 1
    for i in range(roc_num - 1, -1, -1):
        print('Seconds left:', i)
    print('Start', roc_num)
    
    
#rocets = int(input())
#roc_num = 0
#for j in range(1, rocets + 1):
    #for i in range(j - 1, -1, -1):
        #print('Seconds left:', i)
    #print('Start', j)