class Hero():
    '''Class to Great Hero for out Game'''
    def __init__(self, name, level, race):
        '''Initiate out hero'''
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        '''Print all parameters of this Hero'''
        discription = (self.name + ' level is: ' + str(self.level) + ' race is: ' + self.race + " Health is: " + str(self.health)).title()
        print(discription)

    def level_up(self):
        '''Upgreat level of Hero'''
        self.level += 1

    def move(self):
        '''Start moving Hero'''
        print('Hero ' + self.name + ' start moving')


class SuperHero(Hero):
    '''Class to great super hero'''
    def __init__(self, name, level, race, magiclevel):
        '''initiate our Super Hero'''
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100


    def makemagic(self):
        '''Use magic'''
        self.magic -= 10

    def show_hero(self):
        discription = (self.name + ' level is: ' + str(self.level) + ' race is: ' + self.race + " Health is: " +
            str(self.health) + ' Magic is: ' + str(self.magic)).title()
        print(discription)


myhero = Hero('Vurdalak', 4, 'Org')
mysuperhero = SuperHero('lala', 10, 'human', 5)
myhero.show_hero()
mysuperhero.show_hero()
mysuperhero.makemagic()
mysuperhero.show_hero()

# myhero1 = Hero('Vurdalak', 5, 'Org')
# myhero2 = Hero('Alexander', 4, 'Human')
# myhero1.show_hero()
# myhero2.move()
# myhero1.level_up()
# myhero1.show_hero()