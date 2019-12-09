import random
from random import randint

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage
        # self.attack_strength = attack_strength

    def attack(self):
        random_attack = random.randint(0, self.max_damage)
        return random_attack

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        return random.randint(0, self.max_block)

class Weapon(Ability):
    def attack(self):
        return randint(self.max_damage//2, self.max_damage)

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
    
    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense
        return self.current_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def add_armor(self, armor):
        self.armors.append(armor)
    
    def og_kills(self, kills):
        self.kills += kills
    
    def og_deaths(self, num_of_deaths):
        self.deaths += deaths

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def attack(self):
        to_attack = 0
        for ability in self.abilities:
            to_attack += ability.attack()
        return to_attack

    def defend(self, damage_amt=0):
        to_block = 0
        for armor in self.armors:
            to_block += armor.block()
        return to_block
    
    def current_health(self):
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
    
    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                
                if opponent.is_alive() == False:
                    self.og_kills(1)
                    opponent.og_deaths(1)
                    print('[ ' + self.name + ' won this round ]')
                else:
                    self.og_kills(1)
                    opponent.og_deaths(1)
                    print('[ ' + opponent.name + ' won this round ]')
            else:
                print('[ draw ]')
                return False

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def index_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    
    def append_hero(self, hero):
        self.heroes.append(hero)

    def pop_hero(self, name):
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
        return 0

    def live_heroes(self):
        live_heroes = []
        for hero in self.heroes:
            if hero.is_alive():
                live_heroes.append(hero)
            return live_heroes

    def attack(self, oteam):
        while len(self.live_heroes()) > 0 and len(oteam.live_heroes()) > 0:
            ateam = random.choice(self.live_heroes())
            bteam = random.choice(oteam.live_heroes())
            #make 'em fight
            ateam.fight(bteam)
    
    def save_the_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health
    
    def stats(self):
        for hero in self.heroes:
            print("hero: " + hero.name)
            print("# of kills: " + str(hero.kills))
            print("# of deaths: {}".format(hero.deaths))

class Arena:
    def __init__(self):
        self.ateam = Team("team uno")
        self.bteam = Team("team dos")

    def create_ability(self):
        ab_name = input("enter ability name: ")
        ab_pwr = input("enter the ability's power (integer): ")
        return Ability(ab_name, int(ab_pwr))

    def create_weapon(self):
        wep_name = input("enter the weapon's name: ")
        wep_pwr = input("enter the weapon's power (integer): ")
        return Weapon(wep_name, int(wep_pwr))
    
    def create_armor(self):
        arm_name = input("enter the armor's name: ")
        arm_pwr = input("enter the armor's power (integer): ")
        return Armor(arm_name, int(arm_pwr))
    
    def create_hero(self):
        hero_name = input("enter the hero's name: ")
        newhero = Hero(hero_name, starting_health=100)
        ab = input("want to add an ability to the hero? (y or n): ").lower()
        if ab == 'y':
            newhero.add_ability(self.create_ability())
        else:
            print('error')
            ab
        wep = input("want to add a weapon to the hero? (y or n): ").lower()
        if ab == 'y':
            newhero.add_weapon(self.create_weapon())
        else:
            print('error')
            wep
        arm = input("want to add an armor to the hero? (y or n): ").lower()
        if ab == 'y':
            newhero.add_armor(self.create_armor())
        else:
            print('error')
            arm
        return newhero

    def construct_ateam(self):
        hamt = input("# of heroes in team uno: ")
        for i in range(0, int(hamt)):
            self.ateam.append_hero(self.create_hero())
    
    def construct_bteam(self):
        bamt = input("# of heroes in team dos: ")
        for i in range(0, int(bamt)):
            self.bteam.append_hero(self.create_hero())
    
    def battle(self):
        self.ateam.attack(self.bteam)
    
    def tdeaths(self, live_team):
        tdeaths = 0
        for hero in live_team:
            if hero.current_health == 0:
                tdeaths += 1
        if tdeaths == len(live_team):
            return True
        else:
            return False
    
    def display(self):
        ateam = self.tdeaths(self.ateam.heroes)
        bteam = self.tdeaths(self.bteam.heroes)

        if ateam == False:
            print(f"the winner of this match is {self.ateam.name}")
            print("survivors of team one: ")
            for hero in live_heroes:
                if hero.is_alive():
                    print(hero.name)
                else:
                    print('everyone is dead')

        elif bteam == False:
            print(f"the winner of this match is {self.bteam.name}")
            print("survivors of team two: ")
            for hero in self.bteam.live_heroes:
                if hero.is_alive():
                    print(hero.name)
                else:
                    print('everyone is dead')
        elif ateam == False and bteam == False:
            print("draw!")

        print(f'team uno kill/death ratio: {self.ateam.stats()}')
        print(f'team dos kill/death ratio: {self.bteam.stats()}')

if __name__ == "__main__":

    #start game
    game = True
    arena = Arena()

    arena.construct_ateam()
    arena.construct_bteam()

    while game:

        arena.battle()
        arena.display()

        again = input('wanna play again? (y or n) ').lower()

        if again == 'y':
            game = True

        else:
            arena.ateam.save_the_heroes()
            arena.bteam.save_the_heroes()
    if game == False:
        again

    ##########

    # TESTS
    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Sophocles", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.abilities)
    # print(ability.name)
    # print(ability.attack())
    # print(hero.attack())
    ##########
    # armor = Armor("Debugging Shield", 10)
    # shield = Armor("[shield_ls_1]", 20)
    # print(armor.name)
    # print(armor.block())
    ##########
    # my_hero = Hero("Sophocles", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    ##########
    # hero = Hero("Themistoklis", 200)
    # hero.take_damage(150)
    # print(hero.is_alive())
    # hero.take_damage(15000)
    # print(hero.is_alive())