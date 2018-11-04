from random import randint

class Character():
    def __init__(self,theWeapon):
        self.Weapon = theWeapon
    def attack(self):
        playerMonster.health -= playerChar.Weapon.power
        return("You attacked the dragon. Its health is now",playerMonster.health)

class Archer(Character):
    def __init__(self):
        super().__init__(Arrow())

class Mage(Character):
    def __init__(self):
        super().__init__(Staff())

class Fighter(Character):
    def __init__(self):
        super().__init__(Fists())

###################################

class Race(Character):
    def __init__(self,health,healPower):
        self.health = health
        self.healPower = healPower
    def heal(self):
        self.health += self.healPower
        return("You have chosen to heal yourself. Your health is now",self.health)
    def get_healPower(self):
        return(self.healPower)
    def get_health(self):
        return(self.health)


class Dwarf(Race):
    def __init__(self):
        super().__init__(70,50)

class Human(Race):
    def __init__(self):
        super().__init__(60,60)

class Elf(Race):
    def __init__(self):
        super().__init__(80,40)

###################################

class Weapon():
    def __init__(self,power):
        self.power = power
    def get_power(self):
        return(self.power)

class Staff(Weapon):
    def __init__(self):
        super().__init__(100)

class Arrow(Weapon):
    def __init__(self):
        super().__init__(20)

class Fists(Weapon):
    def __init__(self):
        super().__init__(30)

class Breath(Weapon):
    def __init__(self):
        super().__init__(120)

##############################

class Monster():
    def __init__(self,health,theWeapon):
        self.Weapon = theWeapon
        self.health = health
    def get_health(self):
        return(self.health)
    def monster_turn(self):
        turn = randint(0,4)
        if turn == 0:
            if warChoice == "2":
                return("The dragon tried to attack you but you blocked it. Well done.")
            else:
                playerRace.health -= 120
                return("The dragon's breath got you. Your health is now",playerRace.health)
        else:
            return("The dragon missed...You are safe")

class Dragon(Monster):
    def __init__(self):
        super().__init__(200,Breath())

playerMonster = Dragon()
raceChoice = input('''You are fighting a dragon...
Choose your Race:
1.Dwarf
Health: 70   Heal Power: 50\n
2.Human
Health: 60   Heal Power: 60\n
3.Elf
Health: 80   Heal Power: 40\n''')

while raceChoice not in ["1","2","3"]:
    raceChoice = input("Please try again\n")

if raceChoice == "1":
    playerRace = Dwarf()
elif raceChoice == "2":
    playerRace = Human()
elif raceChoice == "3":
    playerRace = Elf()

charChoice = input('''Weapons:
Arrow
Power: 20   Attack: Shoot\n
Fists
Power: 30   Attack: Punch\n
Staff
Power: 100  Attack: Blast\n
Choose your Character:
1.Archer
Weapon: Arrow\n
2.Fighter
Weapon: Fists\n
3.Mage
Weapon: Staff\n
''')

while charChoice not in ["1","2","3"]:
    charChoice = input("Please try again\n")

if charChoice == "1":
    playerChar = Archer()
    #print(playerChar.Weapon.get_attackName())
elif charChoice == "2":
    playerChar = Fighter()
    #print(playerChar.Weapon.get_attackName())
elif charChoice == "3":
    playerChar = Mage()
    #print(playerChar.Weapon.get_attackName())

while True:
    warChoice = input('''1.Attack
2.Block
3.Heal\n''')

    while warChoice not in ["1","2","3"]:
        warChoice = input("Please try again\n")

    if warChoice == "1":
        print(playerChar.attack())
    elif warChoice == "3":
        print(playerRace.heal())

    print(Dragon().monster_turn())
    if playerRace.health <= 0:
        print("Game over. You lose.")
        break
    elif playerMonster.health <= 0:
        print("You have slayed the dragon. You win.")
        break

#print(Elf().heal())
#print(Elf().health)

#print(Dragon().health - playerChar.Weapon.power)
#print(Dragon().health)
