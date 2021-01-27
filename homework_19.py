# 1
class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range
    def hit(self, actor, target):
        if target.is_alive():
            first = actor.get_coords()
            second = target.get_coords()
            h = ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) ** 0.5
            if h > self.range:
                print(f'target is too far for weapon {self.name}')
            else:
                print(f'enemy was hit from weapon {self.name}, damage is {self.damage}')
                target.get_damage(self.damage)
        else:
            print("the enemy is already defeated")
    def __str__(self):
        return self.name

class BaseCharacter:
    def __init__(self, pos_x, pos_y, hp):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = hp
    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y
    def is_alive(self):
        return self.hp != 0
    def get_damage(self, amount):
        if self.hp - amount >= 0:
            self.hp -= amount
        else:
            self.hp = 0
    def get_coords(self):
        return self.pos_x, self.pos_y

class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon
    def hit(self, target):
        if isinstance(target, MainHero):
            self.weapon.hit(self, target)
        else:
            print('I can hit only main hero')
    def __str__(self):
        return f'enemy is in the position ({self.pos_x}, {self.pos_y}) with weapon {self.name}'

class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = []
        self.number = 0
    def hit(self, target):
        if isinstance(target, BaseEnemy):
            if len(self.weapon) == 0:
                print('I am unarmed')
            elif isinstance(target, BaseEnemy):
                self.weapon[0].hit(self, target)
        else:
            print('I can hit only enemy')
    def add_weapon(self, weapon):
        if isinstance(weapon, Weapon):
            self.weapon.append(weapon)
            print(f"picked up {weapon}")
        else:
            print("It's not a Weapon")
    def next_weapon(self):
        if len(self.weapon) == 0:
            print('I am unarmed')
        elif len(self.weapon) == 1:
            print('I have one weapon')
        else:
            self.weapon.append(self.weapon.pop(0))
            print(f"i take weapon {self.weapon[0]}")
    def heal(self, amount):
        if self.hp + amount >= 200:
            self.hp = 200
        else:
            self.hp += amount
        print(f'now my health is {self.hp}')



weapon1 = Weapon("Короткий меч", 5, 1)
weapon2 = Weapon("Длинный меч", 7, 2)
weapon3 = Weapon("Лук", 3, 10)
weapon4 = Weapon("Лазерная орбитальная пушка", 1000, 1000)
princess = BaseCharacter(100, 100, 100)
archer = BaseEnemy(50, 50, weapon3, 100)
armored_swordsman = BaseEnemy(10, 10, weapon2, 500)
archer.hit(armored_swordsman)
armored_swordsman.move(10, 10)
print(armored_swordsman.get_coords())
main_hero = MainHero(0, 0, "Король Артур", 200)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.add_weapon(weapon1)
main_hero.hit(armored_swordsman)
main_hero.add_weapon(weapon4)
main_hero.hit(armored_swordsman)
main_hero.next_weapon()
main_hero.hit(princess)
main_hero.hit(armored_swordsman)
main_hero.hit(armored_swordsman)