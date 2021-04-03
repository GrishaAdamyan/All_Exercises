from random import randint

num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 1]

def RoyalFlush(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    suits = [combination[i][1] for i in range(len(combination))]
    if 10 in nums and 'J' in nums and 'Q' in nums and 'K' in nums and 1 in nums:
        for i in range(len(suits)):
            if suits.count(suits[i]) >= 5:
                print('Royal Flush')
                break
    else:
        StraightFlush(combination)

def StraightFlush(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    suits = [combination[i][1] for i in range(len(combination))]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if num.index(nums[i]) > num.index(nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    t = 5
    start, end = 0, 0 + t
    while end < len(nums):
        if nums[start:end] in num:
            for i in range(len(suits)):
                if suits.count(suits[i]) >= 5:
                    print('Straight Flush')
                    break
        start += 1
        end += 1
    else:
        FourOfAKind(combination)

def FourOfAKind(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    for elem in set(nums):
        if nums.count(elem) == 4:
            print('Four Of A Kind')
            break
    else:
        FullHouse(combination)

def FullHouse(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    list1 = []
    for elem in nums:
        list1.append(nums.count(elem))
    if 3 in list1 and 2 in list1:
        print('Full House')
    else:
        Flush(combination)

def Flush(combination):
    suits = [combination[i][1] for i in range(len(combination))]
    for i in range(len(suits)):
        if suits.count(suits[i]) >= 5:
            print('Flush')
            break
    else:
        Straight(combination)

def Straight(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if num.index(nums[i]) > num.index(nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    t = 5
    start, end = 0, 0 + t
    while end < len(nums):
        if nums[start:end] in num:
            print('Straight')
        start += 1
        end += 1
    else:   
        ThreeOfAKind(combination)

def ThreeOfAKind(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    for elem in set(nums):
        if nums.count(elem) == 3:
            print('Three Of A Kind')
            break
    else:
        TwoPair(combination)

def TwoPair(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    list1 = []
    for elem in nums:
        list1.append(nums.count(elem))
    if list1.count(2) >= 2:
        print('Two Pair')
    else:
        Pair(combination)

def Pair(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    list1 = []
    for elem in nums:
        list1.append(nums.count(elem))
    if list1.count(2) == 1:
        print('Pair')
    else:    
        HighCard(combination)

def HighCard(combination):
    nums = [combination[i][0] for i in range(len(combination))]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if num.index(nums[i]) > num.index(nums[j]):
                nums[i], nums[j] = nums[j], nums[i]
    print('High Card')






print('Hello player. You will now play well known Poker game.')
cards = [[1, 'Club'], [2, 'Club'], [3, 'Club'], [4, 'Club'], [5, 'Club'], [6, 'Club'], [7, 'Club'], [8, 'Club'], [9, 'Club'], [10, 'Club'], ['J', 'Club'], ['Q', 'Club'], ['K', 'Club'], [1, 'Spade'], [2, 'Spade'], [3, 'Spade'], [4, 'Spade'], [5, 'Spade'], [6, 'Spade'], [7, 'Spade'], [8, 'Spade'], [9, 'Spade'], [10, 'Spade'], ['J', 'Spade'], ['Q', 'Spade'], ['K', 'Spade'], [1, 'Heart'], [2, 'Heart'], [3, 'Heart'], [4, 'Heart'], [5, 'Heart'], [6, 'Heart'], [7, 'Heart'], [8, 'Heart'], [9, 'Heart'], [10, 'Heart'], ['J', 'Heart'], ['Q', 'Heart'], ['K', 'Heart'], [1, 'Diamond'], [2, 'Diamond'], [3, 'Diamond'], [4, 'Diamond'], [5, 'Diamond'], [6, 'Diamond'], [7, 'Diamond'], [8, 'Diamond'], [9, 'Diamond'], [10, 'Diamond'], ['J', 'Diamond'], ['Q', 'Diamond'], ['K', 'Diamond']]

player_card = []
for i in range(2):
    card = randint(0, len(cards) - 1)
    player_card += [cards[card]]
    cards.remove(cards[card])
print(player_card)

AI_card = []
for i in range(2):
    card = randint(0, len(cards) - 1)
    AI_card += [cards[card]]
    cards.remove(cards[card])

cards_for_table = []
for i in range(5):
    card = randint(0, len(cards) - 1)
    cards_for_table += [cards[card]]
    cards.remove(cards[card])
print(cards_for_table)

player_and_table_cards = player_card + cards_for_table
AI_and_table_cards = AI_card + cards_for_table
RoyalFlush(player_and_table_cards)