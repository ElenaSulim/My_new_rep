from My_new_rep.Class_Auto.Auto import Auto
import time
class Truck(Auto):
    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)