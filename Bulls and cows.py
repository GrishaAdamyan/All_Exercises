#word1 = input()
#word2 = input()
#bulls = 0
#cows = 0
#for i in range(len(word1)):
    #if word1[i] == word2[i]:
        #bulls += 1
    #elif word1[i] in word2:
        #cows += 1
#print(bulls,cows)

word1 = input()
word2 = input()
bulls = 0
cows = 0
for i in range(len(word1)):
    if word1[i] == word2[i]:
        bulls += 1
set3 = set(word1) & set(word2)
print(set3)
cows = len(set3) - bulls
print(bulls,cows)
#piton
#pilot	
#3 1