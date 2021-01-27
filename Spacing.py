def space_game(text):
    count = 0
    text = input()
    for i in range(len(text)):
        if text[i] = ' ':
            count += 1
    if count % 2 == 0:
        print('You win')
    else:
        print('You lose')
space_game()