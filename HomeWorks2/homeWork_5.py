

class Vehicle:
    def start(self):
        print('Транспорт запускается')


class Car(Vehicle):
    def start(self):
        super().start()
        print('Автомобиль запускается')


class ElectricCar(Vehicle):
    def start(self):
        super().start()


class Tesla(ElectricCar, Car):
    def start(self):
        super().start()
        print('Tesla готова к движению')



Tesla().start()


