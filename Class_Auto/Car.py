from My_new_rep.Class_Auto.Auto import Auto

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        print('Move')
        print(self.max_speed)