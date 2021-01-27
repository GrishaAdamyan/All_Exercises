from random import randint
import LISTS_FOR_ROCK_PAPER_SCISSORS_GAME


languages = LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[12:]
language = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[10])
while language not in languages:
    language = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[11])
if language == 'ENG':
    print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[0])
    def RPS():
        AI_count = 0
        PLAYER_count = 0
        list1 = LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[1:4]
        while AI_count != 20:
            number = randint(0, len(list1) - 1)
            PLAYER_step = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[4])
            while PLAYER_step not in list1:
                PLAYER_step = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[5])
            AI_step = list1[number]
            print(f"AI's step is {AI_step}, player's step is {PLAYER_step}")
            if AI_step == PLAYER_step:
                print(f'Count: {AI_count} - {PLAYER_count}')
            else:
                if AI_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[1]:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[2]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[7])
                        AI_count += 1
                elif AI_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[2]:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[3]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[7])
                        AI_count += 1
                else:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[1]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[7])
                        AI_count += 1
                print(f'Count: {AI_count} - {PLAYER_count}')
            if PLAYER_count == 20:
                break
        return LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[8] if AI_count == 20 else LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ENG_LIST[9]
    
    
    print(RPS())


elif language == 'РУС':
    print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[0])
    def RPS():
        AI_count = 0
        PLAYER_count = 0
        list1 = LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[1:4]
        while AI_count != 20:
            number = randint(0, len(list1) - 1)
            PLAYER_step = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[4])
            while PLAYER_step not in list1:
                PLAYER_step = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[5])
            AI_step = list1[number]
            print(f"AI's step is {AI_step}, player's step is {PLAYER_step}")
            if AI_step == PLAYER_step:
                print(f'Count: {AI_count} - {PLAYER_count}')
            else:
                if AI_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[1]:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[2]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[7])
                        AI_count += 1
                elif AI_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[2]:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[3]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[7])
                        AI_count += 1
                else:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[1]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[7])
                        AI_count += 1
                print(f'Count: {AI_count} - {PLAYER_count}')
            if PLAYER_count == 20:
                break
        return LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[8] if AI_count == 20 else LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.РУС_LIST[9]
    
    
    print(RPS())

else:
    print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[0])
    def RPS():
        AI_count = 0
        PLAYER_count = 0
        list1 = LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[1:4]
        while AI_count != 20:
            number = randint(0, len(list1) - 1)
            PLAYER_step = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[4])
            while PLAYER_step not in list1:
                PLAYER_step = input(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[5])
            AI_step = list1[number]
            print(f"AI's step is {AI_step}, player's step is {PLAYER_step}")
            if AI_step == PLAYER_step:
                print(f'Count: {AI_count} - {PLAYER_count}')
            else:
                if AI_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[1]:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[2]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[7])
                        AI_count += 1
                elif AI_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[2]:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[3]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[7])
                        AI_count += 1
                else:
                    if PLAYER_step == LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[1]:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[6])
                        PLAYER_count += 1
                    else:
                        print(LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[7])
                        AI_count += 1
                print(f'Count: {AI_count} - {PLAYER_count}')
            if PLAYER_count == 20:
                break
        return LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[8] if AI_count == 20 else LISTS_FOR_ROCK_PAPER_SCISSORS_GAME.ՀԱՅ_LIST[9]
    
    
    print(RPS())