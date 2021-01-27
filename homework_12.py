# 1
def newRoadSystem(roadRegister):
    total1 = [sum(x) for x in roadRegister]
    total2 = [sum(x) for x in zip(*roadRegister)]
    return total1 == total2


print(newRoadSystem([[False, True, False, False], 
                     [False, False, True, False], 
                     [True, False, False, True], 
                     [False, False, True, False]]))


# 2
#def efficientRoadNetwork(n, roads):
    #for i in range(n):
        #for j in range(i + 1, n):
            #if [i, j] in roads or [j, i] in roads:
                #continue
            #else:
                #for k in range(n):
                    #if ([i, k] in roads and [k, j] in roads):
                        #break
                    #elif ([i, k] in roads and [j, k] in roads):
                        #break
                    #elif ([k, i] in roads and [k, j] in roads):
                        #break
                    #elif ([k, i] in roads and [j, k] in roads):
                        #break
                #else:
                    #return False
    #return True


#print(efficientRoadNetwork(6, [[3,0], 
                               #[0,4], 
                               #[5,0], 
                               #[2,1], 
                               #[1,4], 
                               #[2,3], 
                               #[5,2]]))