import random
from typing import Union, Dict, Any
from config import person_names
from things import things, my_things


class Person:
    """Базовый класс всех героев."""

    def __init__(self, name, health, base_attack, base_proto) -> None:
        self.name: str = name
        self.health: float = health
        self.base_attack: float = base_attack
        self.base_proto: float = round(base_proto, 1)

    def set_things(self, thing: Dict) -> tuple[Union[float, Any],
                                               Union[float, Any],
                                               Union[float, Any]]:
        """Метод одевания шмота."""

        if thing in things:
            self.health = self.health + things[thing].health
            self.base_attack = self.base_attack + things[thing].attack
            self.base_proto = self.base_proto + (things[thing].proto * 100)
        return self.health, self.base_attack, self.base_proto

    def damage(self, persons) -> None:
        """Метод получения урона."""

        self.health = self.health - persons.base_attack


class Paladin(Person):
    """Подкласс паладин."""

    COEFF_HEALTH = 2
    COEFF_PROTO = 2

    def __init__(self, name, health, base_attack, base_proto):
        super().__init__(name, health, base_attack, base_proto)
        self.health = health * self.COEFF_HEALTH
        self.base_proto = base_proto * self.COEFF_PROTO


class Warrior(Person):
    """Подкласс война."""

    COEFF_ATTACK = 2

    def __init__(self, name, health, base_attack, base_proto):
        super().__init__(name, health, base_attack, base_proto)
        self.base_attack = self.base_attack * self.COEFF_ATTACK


def create_warrior(health: int, attack: float, proto: float) -> Person:
    """Функция обьявления экземпляра война."""

    warrior = Warrior(random.choice(person_names), health, attack, proto)
    for name in person_names:
        if warrior.name == name:
            person_names.remove(name)
            break
    return warrior


def create_paladin(health: int, attack: float, proto: float) -> Person:
    """Функция обьявления экземпляра Паладина."""

    name = random.choice(person_names)
    paladin = Paladin(name, health, attack, proto)
    for names in person_names:
        if paladin.name == names:
            person_names.remove(names)
            break
    return paladin


def get_secret(heroes):
    """Функция расчёта получения количества шмота
        и рандомного полученя шмота."""

    for thing in things:
        rand = random.randint(1, 4)
        print(f"Боец с именем {heroes.name} берет {rand + 1} вещи "
              f"из сундука")
        incr = 0
        while incr <= rand:
            """ Здесь идёт получение рандомного шмота с описанием 
                        инкремента их свойств классам."""

            secret = random.choice(my_things)
            hero.set_things(secret)
            print(f"{heroes.name} берет {secret} из сундука, теперь у него "
                  f"{heroes.base_attack} дамага, {round(heroes.base_proto)} защиты,"
                  f"{heroes.health} здоровья")
            incr += 1
        break


"""Просто чистый лист героев."""

my_heroes = list()

"""Создание 5 паладинов и 5 войнов с рандомными 
    именами добавлением в список."""
for person in person_names:
    if len(my_heroes) <= 5:
        hero = create_paladin(1500, 300, 45)
        my_heroes.append(hero)
    elif 5 < len(my_heroes) <= 10:
        hero = create_warrior(1000, 800, 20)
        my_heroes.append(hero)
    elif 10 < len(my_heroes):
        break

""" Здесь вывод оствшихся 10 героев, которые не учавствуют в бою."""

print("___________________________________________________")
print(f"Ожидают часа бойни в своих кельях следующие войны: ")
for i in person_names:
    print(i)

"""Список с живыми героями в бою 1*1."""

life_hero = list()
"""Основной цикл. Выборка по 2 героя."""

for hero in my_heroes:
    life_hero.append(hero)
    a = True
    if len(life_hero) == 2:
        """Функция получения шмота 1 и 2 героем."""

        get_secret(life_hero[1])
        get_secret(life_hero[0])
        """Цикл сражения с принтами в консоль."""

        while a:
            life_hero[0].damage(life_hero[1])
            print(f"Герой с именем {life_hero[0].name} получил дамага от "
                  f"{life_hero[1].name} в размере {life_hero[1].base_attack} "
                  f"и у него осталось здоровья {life_hero[0].health}")
            """При смерти первого героя он удаляется из списка."""

            if life_hero[0].health <= 0:
                print(f"{life_hero[0].name} умирает")
                del life_hero[0]
                a = False
                break
            life_hero[1].damage(life_hero[0])
            print(f"Герой с именем {life_hero[1].name} получил дамага от "
                  f"{life_hero[0].name} в размере {life_hero[0].base_attack} "
                  f"и у него осталось здоровья {life_hero[1].health}")
            """При смерти Второго героя он удаляется из списка."""

            if life_hero[1].health <= 0:
                print(f"{life_hero[1].name} умирает")
                del life_hero[1]
                a = False
                break
print(f"Победителем состязаний становится... {life_hero[0].name}")
