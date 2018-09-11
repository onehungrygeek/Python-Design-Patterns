import time


class ResourceHeavyClass:
    def busy(self):
        print("Class busy!")

    def ready(self):
        print("Class ready!")


class Proxy:
    def __init__(self):
        self.occupied = False
        self.heavywork = None

    def check(self):
        print("Checking...")
        if not self.occupied:
            self.heavywork = ResourceHeavyClass()
            time.sleep(3)
            self.heavywork.ready()
        else:
            time.sleep(3)
            print("Class still busy!")


p = Proxy()
p.check()
p.occupied = True
p.check()
