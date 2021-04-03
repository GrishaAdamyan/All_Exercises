def madlib1():
    print("Story's name The Photographer")
    animals= input('enter a animal name: ')
    profession = input('enter a profession name: ')
    cloth = input('enter a piece of cloth name: ')
    things = input('enter a thing name: ')
    name= input('enter a name: ')
    place = input('enter a place name: ')
    verb = input('enter a verb in ing form: ')
    food = input('food name: ')
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind.')


def madlib2():
    print("Story's name The Butterfly")
    adjective = input('enter adjective: ')
    color = input('enter a color name: ')
    thing = input('enter a thing name: ')
    place = input('enter a place name: ')
    person= input('enter a person name: ')
    adjective1 = input('enter a adjective: ')
    insect= input('enter a insect name: ')
    food = input('enter a food name: ')
    verb = input('enter a verb name: ')

    print('Last night I dreamed I was a ' +adjective+ ' butterfly with ' +color+ ' splocthes that looked like ' +thing+'. I flew to ' +place+ ' with my bestfriend and ' +person+ ' who was a ' +adjective1+' ' +insect +'. We ate some ' +food+ ' when we got there and then decided to ' +verb+ ' and the dream ended when I said-- lets ' +verb+'.')


def madlib3():
    print("Story's name apple and apple")
    person = input('enter person name: ')
    color = input('enter color: ')
    foods = input('enter food name: ')
    adjective = input('enter a adjective name: ')
    thing = input('enter a thing name: ')
    place = input('enter place: ')
    verb = input('enter verb: ')
    adverb = input('enter adverb: ')
    food = input('enter food name: ')
    things = input('enter a thing name: ')
   
    print('Today we picked apple from '+person+ "'s Orchard. I had no idea there were so many different varieties of apples. I ate " +color+ ' apples straight off the tree that tested like '+foods+ '. Then there was a '+adjective+ ' apple that looked like a ' + thing + '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to ' +verb+ ' ' +adverb+ '. I can hardly wait to get home and cook with the apples. We are going to make apple '+food+ ' and '+things+' pies!.')

print('Hello player. You will now play the well known Mad Libs Generator game.') # Txeq ete krnaq targmaneq @stex anglerenov es xaxi kanonner@ greq. Ete es grem bdi Google Translate-ov grem @dik krna sxal exni.
print('Enter number in range 1-3')
num = int(input())
while not 1 <= num <= 3:
    print('Wrong number. Enter number in range 1-3')
    num = int(input())
if num == 1:
    madlib1()
elif num == 2:
    madlib2()
else:
    madlib3()