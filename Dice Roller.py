from random import randint

def Dice_Roller():
    print('Hello player. Now you start roll the dice and computer will calculate count of even and odd numbers, if value is even count will increase by 1, otherwise count will be reduced by 1, If count will 10 you win, if count will -10 you lose')
    print('Start')
    count = 0
    value = randint(1, 6)
    while count != 10:
        print('Value =', value)
        if value % 2 == 1:
            count -= 1
        elif value % 2 == 0:
            count += 1
        if count == -10:
            return 'You lose'
        print('Count =', count)
        value = randint(1, 6)
    return 'You win'


print(Dice_Roller())