import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        # self.attack_strength = attack_strength

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        random_block = random.randint(0, self.max_block)
        return random_block #self.max_block

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    
    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def attack(self):
        return sum(ability.attack() for ability in self.abilities)

    def defend(self, damage_amt):
        return sum(armor.block() for armor in self.armors)

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    
    def fight(self, opponent):
        while True:
            

if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    another_ability = Ability("Smarty Pants", 90)
    hero = Hero("Sophocles", 200)
    hero.add_ability(ability)
    hero.add_ability(another_ability)
    print(hero.abilities)
    print(ability.name)
    print(ability.attack())
    print(hero.attack())
    ##########
    armor = Armor("Debugging Shield", 10)
    shield = Armor("[shield_ls_1]", 20)
    print(armor.name)
    print(armor.block())
    ##########
    my_hero = Hero("Sophocles", 200)
    print(my_hero.name)
    print(my_hero.current_health)
    ##########
    hero = Hero("Themistoklis", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())