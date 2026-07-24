"""
LESSON 2: Inheritance
Inheritance allows a Child class to inherit attributes and methods from a Parent class,
reducing code duplication.
"""

# Base Parent Class
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print(f"🗡️ {self.name} attacks dealing {self.attack_power} damage!")

# Child Class inheriting from Enemy
class Dragon(Enemy):
    def __init__(self, name, health, attack_power, fire_damage):
        # super() calls the Parent class __init__ method
        super().__init__(name, health, attack_power)
        self.fire_damage = fire_damage

    # Method Overriding: Replacing parent class behavior with custom behavior
    def attack(self):
        print(f"🔥 {self.name} breathes fire dealing {self.attack_power + self.fire_damage} fire damage!")

    def fly(self):
        print(f"🦇 {self.name} takes to the skies!")

# Child Class 2
class Goblin(Enemy):
    def steal_gold(self, target_player):
        print(f"💰 {self.name} sneaks up and steals 10 gold!")

# Testing the hierarchy
basic_goblin = Goblin("Sneaky Bob", health=30, attack_power=8)
red_dragon = Dragon("Ignis", health=300, attack_power=40, fire_damage=25)

basic_goblin.attack()      # Uses parent method
basic_goblin.steal_gold("Player1")

red_dragon.attack()        # Uses overridden dragon method
red_dragon.fly()

# ✏️ PRACTICE EXERCISE:
# Create a 'BossEnemy' child class that inherits from Enemy and gets a special 'phase_two()' method
# that doubles its attack power when health drops below 50%!
