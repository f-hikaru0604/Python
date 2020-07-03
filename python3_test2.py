class vehicle:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def move_on(self):
        print(self.name,'は',self.action,'と進みます')

class automobile(vehicle):
    def move_on(self):
        super().move_on()

class bicycle(vehicle):
    def move_on(self):
        super().move_on()

class ship(vehicle):
    def move_on(self):
        super().move_on()

class airplane(vehicle):
    def move_on(self):
        super().move_on()

am = automobile('自動車','アクセルを踏む')
am.move_on()
bc = bicycle('自転車','ペダルを漕ぐ')
bc.move_on()
sh = ship('船','スクリューを回す')
sh.move_on()
ap = airplane('飛行機','プロペラを回す')
ap.move_on()