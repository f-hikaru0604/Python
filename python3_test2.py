class Vehicle:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def move_on(self):
        pass

class Automobile(Vehicle):
    def move_on(self):
        print(self.name,'は',self.action,'と進みます')

class Bicycle(Vehicle):
    def move_on(self):
        print(self.name,'は',self.action,'と進みます')

class Ship(Vehicle):
    def move_on(self):
        print(self.name,'は',self.action,'と進みます')

class Airplane(Vehicle):
    def move_on(self):
        print(self.name,'は',self.action,'と進みます')

am = Automobile('自動車','アクセルを踏む')
am.move_on()
bc = Bicycle('自転車','ペダルを漕ぐ')
bc.move_on()
sh = Ship('船','スクリューを回す')
sh.move_on()
ap = Airplane('飛行機','プロペラを回す')
ap.move_on()