class Horse:       # класс описывающий лошадь
    def __init__(self): # x_distance = 0 - пройденный путь.                                               # sound = 'Frrr' - звук, который издаёт лошадь.
        super().__init__()
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle:        # класс описывающий орла
    def __init__(self):
        super().__init__()
        self.y_distance = 0                                #_distance = 0 - высота полёта
        sound = 'I train, eat, sleep, and repeat'   # sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)

    def fly(self, dy):               #  dy - изменение дистанции, увеличивает y_distance на dy
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):          # класс описывающий пегаса
    def __init__(self):
        super().__init__()
        Eagle.__init__(self)

    def move(self, dx, dy):          # где dx и dy изменения дистанции
        return self.run(dx), self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance  # возвращает текущее положение пегаса в виде кортежа

    def voice(self):
        print({self.sound})


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
