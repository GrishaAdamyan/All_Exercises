from random import randint

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
def guess():
    print('Hello player. You will now play the well known Number Guesing game. The player must guess the number in the range of 1-100 in 7 steps. After saying each number, the player will be prompted, that number is greater than the memorized number or the opposite')
    print('Start')
    count = 0
    guested_number = randint(1, 100)
    while count != 7:
        num = int(input('Enter number in the range of 1-100: '))
        while num not in nums:
            num = input('Wrong number. Enter number in the range of 1-100: ')
        if guested_number == num:
            return 'YOU WIN'
        else:
            if guested_number > num:
                print('Guested number greater than that number')
            else:
                print('Guested number smaller than that number')
            count += 1
        print('You have', 7 - count, 'chances')
    return 'YOU LOSE'


print(guess())