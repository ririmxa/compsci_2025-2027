class Character:
    def __init__(self, name, health, basic_attack):
        self.__name = name
        self.__health = health
        self.__basic_attack = basic_attack
    def get_name(self):
        return self.__name
    def get_health(self):
        return self.__health
    def get_attack(self):
        return self.__basic_attack
    def set_health(self, health):
        self.__health = max(0, health)
    def take_damage(self, damage):
        self.set_health(self.get_health() - damage)
    def is_alive(self):
        if self.get_health() > 0:
            return True
        else:
            return False
        
class SuperSoldier(Character):
    def __init__(self, name, health, basic_attack, mana):
        super().__init__(name, health, basic_attack)
        self.__mana = mana
    def get_mana(self):
        return self.__mana
    def set_mana(self, mana):
        self.__mana = max(0, mana)
    def special_attack(self, target):
        if self.get_mana() >= 10:
            damage = self.get_attack() * 2
            self.set_mana(self.__mana - 10)
        else:
            damage = self.get_attack()
        target.take_damage(damage)

class Metal(Character):
    def __init__(self, name, health, basic_attack, armour):
        super().__init__(name, health, basic_attack)
        self.__armour = armour

    def get_armour(self):
        return self.__armour

    def set_armour(self, armour):
        self.__armour = max(0, armour)

    def special_attack(self, target):
        self.__armour += 5
        target.take_damage(self.get_attack())

class Party:
    def __init__(self):
        self.__members = []

    def add_member(self, character):
        self.__members.append(character)

    def party_stats(self):
        for member in self.__members:
            print(f"{member.get_name()} | Health: {member.get_health()}")

char1 = Character("Iron Man", 100, 20)
char2 = SuperSoldier("Captain America", 120, 15, 30)

turn = 0
while char1.is_alive() and char2.is_alive():
    if turn % 2 == 0:
        char2.take_damage(char1.get_attack())
        print(f"{char1.get_name()} attacks {char2.get_name()} for {char1.get_attack()} damage. {char2.get_name()} has {char2.get_health()} health left.")
    else:
        char1.take_damage(char2.get_attack())
        print(f"{char2.get_name()} attacks {char1.get_name()} for {char2.get_attack()} damage. {char1.get_name()} has {char1.get_health()} health left.")
    turn += 1

if char1.is_alive():
    print(f"{char1.get_name()} wins!")
else:
    print(f"{char2.get_name()} wins!")
        