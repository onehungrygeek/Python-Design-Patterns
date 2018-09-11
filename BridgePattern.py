class DrawAPIOne(object):
    def drawCircle(self, x, y, radius):
        print("Drawing using API1...")


class DrawAPITwo(object):
    def drawCircle(self, x, y, radius):
        print("Drawing using API2...")


class Circle(object):
    def __init__(self, x, y, radius, drawAPI):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawAPI = drawAPI

    def draw(self):
        self._drawAPI.drawCircle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent


circle1 = Circle(1, 2, 3, DrawAPIOne())
circle1.draw()

circle2 = Circle(2, 3, 4, DrawAPITwo())
circle2.draw()
