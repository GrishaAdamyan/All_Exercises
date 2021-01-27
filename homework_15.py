# 1
class User:
    def __init__(self, name):
        self.name = name
    def send_message(self, user, message):
        print(message, 'sended')
    def post(self, message):
        print(message, 'posted')
    def info(self):
        print('')
    def describe(self):
        print(self.name)



class Person(User):
    def __init__(self, name, birthday):
        super().__init__(name)
        self.birthday = birthday
    def info(self):
        print('Person was born on', self.birthday)
    def subscribe(self, user):
        pass
    
    
    
class Community(User):
    def __init__(self, name, description):
        super().__init__(name)    
        self.description = description
    def info(self):
        print(self.description)


user = User(name = 'Grisha')
p = Person(name = 'Grisha', birthday = 'Feb 25')
c = Community(name = 'Gyumri', description = 'description of Gyumri')
user.post('message')
user.send_message('User', 'message')
user.info()
user.describe()


# 2
class TicTacToe:
    def __init__(self):
        self.list1 = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-'],]
    def new_game(self, list1):
        self.list1 = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-'],]
    def get_field(self, list1):
        print(list1)
    def check_field(self, list1):
        for i in range(len(list1)):
            if list1[i].count('x') == 3:
                return 'x'
            elif list1[i].count('o') == 3:
                return 'o'
        list2 = [[], [], []]
        for i in range(3):
            for j in range(3):
                list2[i].append(list1[j][i])
        for i in range(len(list2)):
            if list2[i].count('x') == 3:
                return 'x'
            elif list2[i].count('o') == 3:
                return 'o'
        list3 = [[],[]]
        for j in range(3):
            list3[0].append(list1[j][j])
            list3[1].append(list1[j][3 - 1 - j])
        for i in range(len(list3)):
            if list3[i].count('x') == 3:
                return 'x'
            elif list3[i].count('o') == 3:
                return 'o'
        count = [sum(list1[i].count('x') for i in range(len(list1)))] + [sum(list1[i].count('o') for i in range(len(list1)))]
        if count[0] != 9:
            return None
        return 'd'
    def make_move(self, row, col, list1, list2):
        if list1[row - 1][col - 1] != '-':
            print(f'Cell ({row}, {col}) is already filled')
        else:
            if [sum(list1[i].count('x') for i in range(len(list1)))] <= [sum(list1[i].count('o') for i in range(len(list1)))]:
                list1[row - 1][col - 1] = 'x'
            else:
                list1[row - 1][col - 1] = 'o'
            if list1[row].count('x') == 3:
                print('X-player won!')
            elif list1[row].count('o') == 3:
                print('O-player won!')
            elif list2[col].count('x') == 3:
                print('X-player won!')
            elif list2[col].count('o') == 3:
                print('O-player won!')
            count = [sum(list1[i].count('x') for i in range(len(list1)))] + [sum(list1[i].count('o') for i in range(len(list1)))]
            if count[0] != 9:
                print('Continue playing')
            else:
                print('Draw')
            print('Game Over')