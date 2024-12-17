import random
from tkinter.font import names


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        print(f'{self.name} атакует {other.name}')
        other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} получает {damage} урона! \n'
              f'Осталось здоровья: {self.health}')

    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, attack_power = 20)

    def special_attack(self,other):
        damage = random.randint(5, self.attack_power * 2)
        print(f'{self.name} выполняет специальную атаку на {other.name}')
        other.take_damage(damage)

class Mage(Character):
    _MAGIC_NAMES = ['Огонь', 'Воздушный кулак', 'Анигиляция']
    def __init__(self, name):
        super().__init__(name, health=70, attack_power=15)

    def cast_spells(self, other):
        damage = random.randint(15, self.attack_power + 25)
        print(f'{self.name} применяет заклинание {self._MAGIC_NAMES[random.randint(0,len(self._MAGIC_NAMES))]} на {other.name}')
        other.take_damage(damage)

def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
        action = random.choice(['attack', 'special_attack'])

        if isinstance(character1, Warrior) and action == 'special_attack':
            character1.special_attack(character2)
        else:
            character1.attack(character2)

        if not character2.is_alive():
            print(f'{character2.name} побежден! Вы одержали победу!!!')
            break

        action = random.choice(['attack', 'special_attack'])
        if isinstance(character2, Warrior) and action == 'special_attack':
            character2.special_attack(character1)
        else:
            character2.attack(character1)

        if not character1.is_alive():
            print(f'{character1.name} побежден! Мы проиграли!!!')
            break

def main():
    print(f'Добро пожаловать в игру ГЕРОИ!')
    player_name = input('Введите имя вашего героя:\n')

    choice = input('Выберите класс (воин / маг)').lower()

    if choice == 'воин':
        player = Warrior(player_name)
    elif choice == 'маг':
        player = Mage(player_name)
    else:
        print('Некорректный выбор, создается воин по умолчанию')
        player = Warrior(player_name)

    enemy = Warrior('Дракон')

    print(f'\n{player_name} начинает бой с {enemy.name}')
    battle(player, enemy)

main()



