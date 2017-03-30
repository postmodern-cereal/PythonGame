#item superclass: has all the abstract stuff we'll need later
class Object:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def change_description(self, description):
        self.description = description

    def change_name(self, name):
        self.name = name

    def __str__(self):
        return "{}:\n{}\n".Format(self.name, self.description)

class Weapon(Object):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage
        #self.kind =  kind #sword, longsword, bow, etc

    def deal_damage(self, enemy):
        enemy.take_damage(self.damage)

    def __str__(self):
        return "{}:\n{}\nDamage: {}".Format(self.name, self.description, self.damage)

class Fists(Weapon):
    def __init__(self):
        super().__init__(name="Fists", description="Your fists. They don't do much damage.", damage=5)

class Armor(object):
    def __init__(self, name, description, protection, kind):
        super().__init__(name, description)
        self.protection = protection
        self.kind = kind #plate, chain mail, hide, etc

    def absorb_damage(self, amount):
        #somehow absorb the damage
        #need:
            # - chance to fully evade
            # - amount to absorb if evade or not
        #return amount_to_absorb

#being inherits object because why not
class Being(Object):
    def __init__(self, name, description, level, health, sex, items, weapon, armor, message):
        super().__init__(name, description)
        self.health = health
        self.level = level
        self.sex = sex
        self.inventory = items #not sure if this is how you do it
        self.weapon = weapon
        self.armor = armor
        self.death_message = message
        #that's male or female, perv

    def heal(self, amount):
        self.health += amount

    def attack(self, enemy):
        self.weapon.deal_damage(enemy)

    def take_damage(self, amount):
        self.health -= (amount - self.armor.absorb(amount))
        if health <= 0:
            self.die

    def die(self):
        print(self.death_message)

class Player(Being):
    # Variables Needed:
    #     - race
    #     - perks
    #     - weapons
    #     - stats
    #     - health
    #     - level
    #     - inventory
    #     - current location
    # Functions Needed:
    #     - init
    #     - add perk
    #     - take damage
    #     - attack
    #     - add to inventory
    #     - equip weapon/armor
    #     - die
    #     - describe self
    #     - change stats
    #     - change level
    def __init__(self, name, description, sex):
        super().__init__(name, description, level=0, health=100, sex, [], none, none, 'You have died')
        self.perks = []
        #self.weapon = fists
        #self.armor = nil
        self.visited = [] #visited locations
        self.location = 'Camp'

    def level_up(self):
        self.level ++
        #increase stats and gain perks or whatever

    def add_Perk(self, perkName):
        self.perks.add(perkName)

    def take_damage(self, amount):
        self.health -= amount
        #use world combat function to test for death

    def attack_enemy(self, enemy):
        enemy.get_damaged(self.weapon.damage)

class Enemy(Being):

    def __init__(self, name, description, level, health, sex, items, weapon, armor, message):
        super().__init__(name, description, level, health, sex, items, weapon, armor, message)

    def hurt_player(self, player):
        player.take_damage(self.damage)

    def get_damaged(self, amount):
        self.health -= amount
        #use world combat function to test for enemy death


def Location(Object):

    # Variables Needed:
    #     - neighbors
    #     - enemy types
    #     - possible drops

    def __init__(self, name, description):
        super().__init__(name, description)
        self.neighbors = []
        self.enemyTypes = []
        self

    #will not really do much with this to start with
    #later on, neighbors will be used to explore the world from location to location
    #for now, locations will be directly accessible from the main base
    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

class World:

    def __init__(self, player):
        self.introduce_Player()
        self.visibleLocations = []
        self.locations = [] #have a method to populate this

    def introduce_Player():
        #need to name player
        #need player's features
        #need player to pick advantages and perks
        #need to tell player what's up
        print("You exist")

    def combat():
        print("Fight!")

def visitLocation(world, player, location):

    #if the player has never visited a location, provide them a description
    if not location in player.visited:
        world.first_description(location)

    #set the player's location to where we are now
    player.set_location(location)
    #make an encounter for the player
    world.create_encounter(player)

def make_new_game():
    print("This is a placeholder method because I can't think")

def quit_game():
    print("Goodbye!")

def beginGame():
    #need to display options
    #print name of game in fancy ASCII art
    print("NEW GAME\t\t\tLOAD GAME\n")
    print("OPTIONS\t\t\t\QUITn")

    choices = {'new' : make_new_game, 'load' : load_game, 'options' : show_options, 'quit' : quit_game}
    choices[input()]()
