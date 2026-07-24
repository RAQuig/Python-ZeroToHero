"""
LESSON 1: Classes & Objects
A class is a custom blueprint for creating objects. Objects bundle data (attributes) 
and functions (methods) together.
"""

class Character:
    # Constructor method (__init__) initializes object attributes when created
    def __init__(self, name, role, hp=100):
        self.name = name          # Instance attribute
        self.role = role          # Instance attribute
        self.hp = hp              # Instance attribute
        self.max_hp = hp          # Instance attribute

    # Instance Method: Function that operates on the object using 'self'
    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"💥 {self.name} took {amount} damage! HP remaining: {self.hp}/{self.max_hp}")

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"✨ {self.name} healed for {amount}! HP: {self.hp}/{self.max_hp}")

    # Special string representation method (controls what print(object) outputs)
    def __str__(self):
        return f"{self.name} the {self.role} [HP: {self.hp}/{self.max_hp}]"

# --- Instantiating (Creating) Objects ---
hero = Character("Aria", "Mage", hp=80)
warrior = Character("Garrick", "Paladin", hp=150)

print(hero)     # Triggers __str__
print(warrior)  # Triggers __str__

hero.take_damage(25)
hero.heal(15)

# ✏️ PRACTICE EXERCISE FOR YOU AND YOUR FRIENDS:
# Add an 'inventory' list attribute to Character, and create a method 'pick_up(item)'
# that appends an item to the list!
