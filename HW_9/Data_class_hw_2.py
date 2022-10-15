class People:
    age = 24

    def some_metod(self):
        print(f'Возраст {self.age}')

    @staticmethod
    def some_metod_2():
        print('Елена')

    @classmethod
    def some_metod_3(cls):
            print('Сулим')

people = People()
people.some_metod()
people.some_metod_2()
people.some_metod_3()






