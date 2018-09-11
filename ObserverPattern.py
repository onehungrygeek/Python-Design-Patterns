class Obeserver:
    def update(self, obj, *args, **kwargs):
        raise NotImplementedError


class Observable:
    def __init__(self):
        self._observers = []

    def addObserver(self, observer):
        self._observers.append(observer)

    def removeObserver(self, observer):
        self._observers.remove(observer)

    def notifyObserver(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)
