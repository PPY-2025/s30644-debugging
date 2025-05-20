class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0

class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def attack(self, target):
        if self.hp == 0:
            print("You can't attack, you're dead")
            return

        damage = int(self.strength * 1.5)
        target.take_damage(damage)

class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def attack(self, target):
        if self.hp == 0:
            print("You can't attack, you're dead")
            return

        if self.mana >= 10:
            target.take_damage(25)
            self.mana -= 10
        else:
            print("Not enough mana!")

def simulate_battle():
    w = Warrior("Thorgal", 100, 10)
    m = Mage("Merlin", 60, 20)

    print("Start:", w.hp, m.hp)
    w.attack(m)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    m.attack(w)
    print("End:", w.hp, m.hp)

# Testy:
def test_simulate_battle():
    w = Warrior("Thorgal", 10, 7)
    m = Mage("Merlin", 20, 20)

    w.attack(m)
    assert m.hp == 10 and w.hp == 10
    w.attack(m)
    assert m.hp == 0
    m.attack(w)
    assert w.hp == 10
    assert m.mana == 20

    m2 = Mage("Gandalf", 20, 20)
    m2.attack(w)
    assert m2.hp == 20 and w.hp == 0
    assert m2.mana == 10

    w.attack(m2)
    assert m2.hp == 20 and w.hp == 0

# Spis błędów i poprawek:
# Błąd 1: Brak castowania na int po wyliczeniu liczby obrażeń w metodzie attack() w obu klasach postaci
# Zmiana 1: Dodano castowanie liczby obrażeń na inta w metodzie attack()

# Błąd 2: metody attack() w obu klasach postaci nie uwzględniają przypadku, w którym hp postaci jest równe 0.
# Zmiana 2: W metodzie attack() dodano warunek:
# jeżeli hp = 0, to postać nie może zaatakować przeciwnika i wyświetli się odpowiedni komunikat.


if __name__ == '__main__':
    simulate_battle()
