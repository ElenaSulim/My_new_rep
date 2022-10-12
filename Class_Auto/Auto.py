class Auto():
    color = 'black'
    weight = 1500


    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('Move')

    def show(self):
        self.move()

    def stop(self):
        print('Stop')

    def show_2(self):
        self.stop()

    def birthday(self):
        self.age += 1
        print('Возраст авто ' + str(self.age))

    def show_3(self):
        self.birthday()





















