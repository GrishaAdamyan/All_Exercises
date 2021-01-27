from random import randint
import Module

languages = ['ENG', 'РУС', 'ՀԱՅ']
print('Enter language for start. Languages are ENG, РУС, ՀԱՅ.')
language = input()
while language not in languages:
    print('False language. Enter language for start. Languages are ENG, РУС, ՀԱՅ.')
    language = input()
if language == 'ENG':
    print('Hello player. You will now play the well known Hangman game. According to the rules of the game, the player must guess the unknown word, for which he has the opportunity to choose a letter 7 times. In case of guessing, the player wins, otherwise he loses. Always enter with UPPERCASES.')
    def hangman():
        while True:
            topics = ['FRUITS', 'ANIMALS', 'COUNTRIES', 'CAPITALS']
            print('Enter topic for start. Topics are FRUITS, ANIMALS, COUNTRIES, CAPITALS.')
            topic = input()
            while topic not in topics:
                print('False topic. Enter topic for start. Topics are FRUITS, ANIMALS, COUNTRIES, CAPITALS.')
                topic = input()
            if topic == 'FRUITS':
                topic = Module.ENG_FRUITS
            elif topic == 'ANIMALS':
                topic = Module.ENG_ANIMALS
            elif topic == 'COUNTRIES':
                topic = Module.ENG_COUNTRIES
            elif topic == 'CAPITALS':
                topic = Module.ENG_CAPITALS
            value = randint(0, len(topic) - 1)
            list1 = ['_' for _ in range(len(topic[value]))]
            print('Unknown word', list1)
            count = 0
            letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            unknown_word = topic[value]
            while list1.count('_') != 0:
                print('Enter letter.')
                l = input()
                while l not in letters:
                    print('Enter letter.')
                    l = input()
                if l in unknown_word:
                    print('True.')
                    letters.remove(l)
                    for i in range(len(unknown_word)):
                        if unknown_word[i] == l:
                            list1[i] = l
                else:
                    print('False.')
                    count += 1
                    letters.remove(l)
                if count == 1:
                    print('''--------
--     -
--
--
--
--
--
--
--
--
--''')
                elif count == 2:
                    print('''--------
--     -
--     -
--   -   -
--     -
--
--
--
--
--
--''')
                elif count == 3:
                    print('''--------
--     -
--     -
--   -   -
--     -
--     -
--     -
--     -
--
--
--''')
                elif count == 4:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - -
--     -
--     -
--
--
--''')
                elif count == 5:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - - -
--     -
--     -
--
--
--''')
                elif count == 6:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - - -
--     -
--     -
--    -
--
--''')
                print('Unknown word', list1)
                if count == 7:
                    print('''--------
--     -
--     -
--   -x x-
--     -
--   - - -
--     -  
--     -
--    - -
--
--''')
                    print('Unknown word is', unknown_word)
                    print('You lose')
                    break
            else:
                print('Unknown word is', unknown_word)
                print('You win')
            print('For starting next game enter NEXT GAME')
            var_for_next_game = input()
            if var_for_next_game == 'NEXT GAME':
                print('Starting next game.')
            else:
                return 'End.'
        
    print(hangman())

elif language == 'РУС':
    print('Привет, игрок. Теперь вы будете играть в хорошо известную игру «Палач». Согласно правилам игры, игрок должен угадать неизвестное слово, для чего у него есть возможность выбрать букву 7 раз. В случае угадывания игрок выигрывает, иначе проигрывает. Всегда вводите ЗАГЛАВНЫМИ буквами.')
    def hangman():
        while True:
            topics = ['ФРУКТЫ', 'ЖИВОТНЫЕ', 'СТРАНЫ', 'СТОЛИЦЫ']
            print('Введите тему для начала. Темы - ФРУКТЫ, ЖИВОТНЫЕ, СТРАНЫ, СТОЛИЦЫ.')
            topic = input()
            while topic not in topics:
                print('Ложная тема. Введите тему для начала. Темы - ФРУКТЫ, ЖИВОТНЫЕ, СТРАНЫ, СТОЛИЦЫ.')
                topic = input()
            if topic == 'ФРУКТЫ':
                topic = Module.РУС_ФРУКТЫ
            elif topic == 'ЖИВОТНЫЕ':
                topic = Module.РУС_ЖИВОТНЫЕ
            elif topic == 'СТРАНЫ':
                topic = Module.РУС_СТРАНЫ
            elif topic == 'СТОЛИЦЫ':
                topic = Module.РУС_СТОЛИЦЫ
            value = randint(0, len(topic) - 1)
            list1 = ['_' for _ in range(len(topic[value]))]
            print('Неизвестное слово', list1)
            count = 0
            letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
            unknown_word = topic[value]
            while list1.count('_') != 0:
                print('Введите букву.')
                l = input()
                while l not in letters:
                    print('Введите букву.')
                    l = input()
                if l in unknown_word:
                    print('ПРАВДА.')
                    letters.remove(l)
                    for i in range(len(unknown_word)):
                        if unknown_word[i] == l:
                            list1[i] = l
                else:
                    print('ЛОЖЬ.')
                    count += 1
                    letters.remove(l)
                if count == 1:
                    print('''--------
--     -
--
--
--
--
--
--
--
--
--''')
                elif count == 2:
                    print('''--------
--     -
--     -
--   -   -
--     -
--
--
--
--
--
--''')
                elif count == 3:
                    print('''--------
--     -
--     -
--   -   -
--     -
--     -
--     -
--     -
--
--
--''')
                elif count == 4:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - -
--     -
--     -
--
--
--''')
                elif count == 5:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - - -
--     -
--     -
--
--
--''')
                elif count == 6:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - - -
--     -
--     -
--    -
--
--''')
                print('Неизвестное слово', list1)
                if count == 7:
                    print('''--------
--     -
--     -
--   -x x-
--     -
--   - - -
--     -  
--     -
--    - -
--
--''')
                    print('Неизвестное слово это', unknown_word)
                    print('Вы проиграли.')
                    break
            else:
                print('Неизвестное слово это', unknown_word)
                print('Вы выиграли.')
            print('Для начала следующей игры введите СЛЕДУЮЩАЯ ИГРА')
            var_for_next_game = input()
            if var_for_next_game == 'СЛЕДУЮЩАЯ ИГРА':
                print('Начало следующей игры.')
            else:
                return 'Конец.'
        
    print(hangman())

else:
    print('Բարև խաղացող: Այժմ դուք խաղալու եք շատերին հայտնի Hangman խաղը: Խաղի կանոնների համաձայն, խաղացողը պետք է գուշակի անծանոթ բառը, որի համար 7 անգամ տառ ընտրելու հնարավորություն ունի: Գուշակելու դեպքում խաղացողը հաղթում է, հակառակ դեպքում նա պարտվում է: Միշտ մուտքագրեք ՄԵԾԱՏԱՌԵՐՈՎ:')
    def hangman():
        while True:
            topics = ['ՄՐԳԵՐ', 'ԿԵՆԴԱՆԻՆԵՐ', 'ԵՐԿՐՆԵՐ', 'ՄԱՅՐԱՔԱՂԱՔՆԵՐ']
            print('Սկսելու համար մուտքագրեք թեմա: Թեմաներ ՝ ՄՐԳԵՐ, ԿԵՆԴԱՆԻՆԵՐ, ԵՐԿՐՆԵՐ, ՄԱՅՐԱՔԱՂԱՔՆԵՐ։')
            topic = input()
            while topic not in topics:
                print('Սխալ թեմա։ Սկսելու համար մուտքագրեք թեմա: Թեմաներ ՝ ՄՐԳԵՐ, ԿԵՆԴԱՆԻՆԵՐ, ԵՐԿՐՆԵՐ, ՄԱՅՐԱՔԱՂԱՔՆԵՐ։')
                topic = input()
            if topic == 'ՄՐԳԵՐ':
                topic = Module.ՀԱՅ_ՄՐԳԵՐ
            elif topic == 'ԿԵՆԴԱՆԻՆԵՐ':
                topic = Module.ՀԱՅ_ԿԵՆԴԱՆԻՆԵՐ
            elif topic == 'ԵՐԿՐՆԵՐ':
                topic = Module.ՀԱՅ_ԵՐԿՐՆԵՐ
            elif topic == 'ՄԱՅՐԱՔԱՂԱՔՆԵՐ':
                topic = Module.ՀԱՅ_ՄԱՅՐԱՔԱՂԱՔՆԵՐ
            value = randint(0, len(topic) - 1)
            list1 = ['_' for _ in range(len(topic[value]))]
            print('Անհայտ բառ', list1)
            count = 0
            letters = ['Ա', 'Բ', 'Գ', 'Դ', 'Ե', 'Զ', 'Է', 'Ը', 'Թ', 'Ժ', 'Ի', 'Լ', 'Խ', 'Ծ', 'Կ', 'Հ', 'Ձ', 'Ղ', 'Ճ', 'Մ', 'Յ', 'Ն', 'Շ', 'Ո', 'Չ', 'Պ', 'Ջ', 'Ռ', 'Ս', 'Վ', 'Տ', 'Ր', 'Ց', 'Ւ', 'Փ', 'Ք', 'և', 'Օ', 'Ֆ']
            unknown_word = topic[value]
            while list1.count('_') != 0:
                print('Մուտքագրեք տառը։')
                l = input()
                while l not in letters:
                    print('Մուտքագրեք տառը։')
                    l = input()
                if l in unknown_word:
                    print('ՃԻՇՏ Է։')
                    letters.remove(l)
                    for i in range(len(unknown_word)):
                        if unknown_word[i] == l:
                            list1[i] = l
                else:
                    print('ՍԽԱԼ Է:')
                    count += 1
                    letters.remove(l)
                if count == 1:
                    print('''--------
--     -
--
--
--
--
--
--
--
--
--''')
                elif count == 2:
                    print('''--------
--     -
--     -
--   -   -
--     -
--
--
--
--
--
--''')
                elif count == 3:
                    print('''--------
--     -
--     -
--   -   -
--     -
--     -
--     -
--     -
--
--
--''')
                elif count == 4:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - -
--     -
--     -
--
--
--''')
                elif count == 5:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - - -
--     -
--     -
--
--
--''')
                elif count == 6:
                    print('''--------
--     -
--     -
--   -   -
--     -
--   - - -
--     -
--     -
--    -
--
--''')
                print('Անհայտ բառ', list1)
                if count == 7:
                    print('''--------
--     -
--     -
--   -x x-
--     -
--   - - -
--     -  
--     -
--    - -
--
--''')
                    print('Անհայտ բառը դա', unknown_word, 'է')
                    print('Դուք պարտվեցիք։')
                    break
            else:
                print('Անհայտ բառը դա', unknown_word, 'է')
                print('Դուք հաղթեցիք։')
            print('Մուտքագրեք ՀԱՋՈՐԴ ԽԱՂ հաջորդ խաղը սկսելու համար:')
            var_for_next_game = input()
            if var_for_next_game == 'ՀԱՋՈՐԴ ԽԱՂ':
                print('ՀԱՋՈՐԴ ԽԱՂԻ ՍԿԻԶԲ։')
            else:
                return 'Վերջ։'
        
    print(hangman())    