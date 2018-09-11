class Director():
    def __init__(self, builder):
        self._builder = builder

    def constructCar(self):
        self._builder.createNewCar()
        self._builder.addModel()
        self._builder.addTires()
        self._builder.addEngine()

    def getCar(self):
        return self._builder.car


class Builder():
    def __init__(self):
        self.car = None

    def createNewCar(self):
        self.car = Car()

class FerrariBuilder(Builder):
    def addModel(self):
        self.car.model = "Ferrari"

    def addTires(self):
        self.car.tires = "Regular Tires"

    def addEngine(self):
        self.car.engine = "Turbo Engine"

class Car():
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None

    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)


builder = FerrariBuilder()
director = Director(builder)
director.constructCar()
car = director.getCar()
print(car)
