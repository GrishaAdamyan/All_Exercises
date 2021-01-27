#n = int(input())
#for i in range(n):
    #text = input()
    #if '%%' in text:
        #print(text[:text.find('%%')] + text[text.find('%%')+2:])
    #elif '####' in text:
        #del text
    #else:
        #print(text)

n = int(input())
for i in range(n):
    text = input()
    if text[:2] == '%%':
        text = text[2:]
    elif text[:4] == '####':
        continue
    print(text)


#n = int(input())
#for i in range(n):
    #text = input()
    #if text[:2] == '%%':
        #print(text[2:])
    #elif text[:4] == '####':
        #continue
    #else:
        #print(text)


#3
#SVO TRS 29481292
#%%LJPZ DME 11113283675
#####&%^^^^

#SVO TRS 29481292
#LJPZ DME 11113283675
