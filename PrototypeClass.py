import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def registerObject(self, name, obj):
        self._objects[name] = obj

    def unRegisterObject(self, name):
        del self._objects[name]

    def cloneObject(self, name, **attr):
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj

class Car:
    def __init__(self):
        self.name = "Ferrari"
        self.color = "Red"
        self.tires = "32mm"

    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.tires)


car = Car()
prototype = Prototype()
prototype.registerObject('ferrari', car)

cloneCar = prototype.cloneObject('ferrari')
print(cloneCar)
