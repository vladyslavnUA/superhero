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

if __name__ == "__main__":
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())