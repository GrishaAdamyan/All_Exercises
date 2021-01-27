#dictionary = {}
#def parrot(phrase):
    #global dictionary
    #if phrase not in dictionary:
        #dictionary[phrase] = 1
    #else:
        #dictionary[phrase] += 1
    #if dictionary[phrase] > 1:
        #print(phrase)


#parrot("Hello")
#parrot("What's your name?")
#parrot("Hello")
#parrot("Hello")



#list1 = []
#def parrot(phrase):
    #list1.append(phrase)
    #if list1.count(phrase) != 1:
        #print(phrase)


#parrot("Hello")
#parrot("What's your name?")
#parrot("Hello")
#parrot("Hello")



list1 = []
def parrot(phrase):
    if phrase in list1:
        print(phrase)
    else:
        list1.append(phrase)


parrot("Hello")
parrot("What's your name?")
parrot("Hello")
parrot("Hello")