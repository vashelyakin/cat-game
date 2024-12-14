import random as r
import sys

class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage  

    def attack(self, opponent):
        hit_chance = r.random()
        if hit_chance < 0.1:
            print(f"{self.name} промахнулся!")
            return 0
        elif hit_chance < 0.3:
            partial_damage = int(self.damage * 0.5)
            print(f"{self.name} нанес частичный урон: {partial_damage}")
            return partial_damage
        elif hit_chance < 0.8:
            print(f"{self.name} нанес урон: {self.damage}")
            return self.damage
        else:
            critical_damage = self.damage * 2
            print(f"{self.name} нанес критический урон: {critical_damage}")
            return critical_damage

class PlayerCat(Character):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.exp = 0  
        self.lvl = 1  

    def create_cat(self, new_rase, new_cls, rase_list, classes):
        if new_rase == rase_list[0]:  
            self.hp = 50
            self.damage = 20
        elif new_rase == rase_list[1]:  
            self.hp = 302
            self.damage = 302
        elif new_rase == rase_list[2]:  
            self.hp = 60
            self.damage = 25
        
        if new_cls == classes[0]:  
            self.hp += 25
            self.damage += 10
        elif new_cls == classes[1]:  
            self.hp += 30
            self.damage += 0
        elif new_cls == classes[2]:  
            self.hp += 10
            self.damage += 15
        elif new_cls == classes[3]:  
            self.hp += 203
            self.damage += 203

    def attack(self, victim):
        max_exp = self.lvl * 100
        change_hit = r.randint(1, 3)
        if change_hit == 1:
            victim.hp -= self.damage
            print(f'You hit the enemy on {self.damage}')
            if victim.hp <= 0:
                print(f"{victim.name} is dead!")
                return False
            else:
                print(f"You have: {self.hp} HP")
                return True
        elif change_hit == 2:
            print(f"You missed!")
            return True
        elif change_hit == 3:
            victim.hp -= self.damage * 2
            print(f'You hit the monster on {self.damage * 2}')
            if victim.hp <= 0:
                print(f"{victim.name} is dead!")
                return False
            else:
                print(f"You have: {self.hp} HP")
                return True

    def levelup(self):
        max_exp = self.lvl * 100
        if self.exp >= max_exp: 
            self.exp -= max_exp  
            self.lvl += 1
            self.hp += 50
            self.damage += 20
            print(f"{self.name} leveled up! Now you're level {self.lvl}, with {self.hp} HP and {self.damage} damage.")
        else:
            print(f"{self.name} doesn't have enough experience to level up.")

class Monster(Character):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

    def attack(self, victim):
        hit_chance = r.random()
        if hit_chance < 0.1:
            print(f"{self.name} промахнулся!")
            return 0
        elif hit_chance < 0.3:
            partial_damage = int(self.damage * 0.5)
            print(f"{self.name} нанес частичный урон: {partial_damage}")
            return partial_damage
        elif hit_chance < 0.8:
            print(f"{self.name} нанес урон: {self.damage}")
            return self.damage
        else:
            critical_damage = self.damage * 2
            print(f"{self.name} нанес критический урон: {critical_damage}")
            return critical_damage

def fight_choice():
    answer = input(f"Do you want to fight with {chosen_monster.name}? Y or n? ").lower()
    if answer == "y":
        result = cat_hero.attack(chosen_monster)
        if result:
            monster_damage = chosen_monster.attack(cat_hero)
            cat_hero.hp -= monster_damage
            if cat_hero.hp <= 0:
                print(f"{cat_hero.name} has died!")
                sys.exit()
        else:
            print("You won the fight!")
            cat_hero.exp += 50  
            print(f"Your experience: {cat_hero.exp}")
            cat_hero.levelup()  
            sys.exit()
    else:
        print(f"You go away from {chosen_monster.name}")
        sys.exit()

rase_list = ["manul", "wild cat", "tiger"]
classes = ["hunter", "lazy cat", "cat wizard", "usual cat"]

name = input("Enter your name: ")
rase = input(f"Choose your race from {rase_list}: ")
cls = input(f"Choose your class from {classes}: ")

cat_hero = PlayerCat(name, 0, 0)
cat_hero.create_cat(rase, cls, rase_list, classes)

print(f"Hello, {cat_hero.name}! Your race is {rase} and you're {cls}. You have {cat_hero.hp} hit points, {cat_hero.damage} points of damage.")

monsters = [
    Monster("Hyena", 80, 15),
    Monster("Snake", 60, 20),
    Monster("Child", 50, 10)
]
chosen_monster = r.choice(monsters)
print(f"\nYou are fighting a {chosen_monster.name}!")

while cat_hero.hp > 0 and chosen_monster.hp > 0:
    print(f"\n{cat_hero.name} has {cat_hero.hp} HP left.")
    print(f"{chosen_monster.name} has {chosen_monster.hp} HP left.")
    fight_choice()

