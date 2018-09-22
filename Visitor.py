class House(object):
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_electricity(self, electrician):
        print(self, "being worked on by", electrician)

    def work_on_plumbing(self, plumber):
        print(self, "being worked on by", plumber)

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    def __str__(self):
        return self.__class__.__name__


class Electrician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


class Plumber(Visitor):
    def visit(self, house):
        house.work_on_plumbing(self)


house = House()
el = Electrician()
pl = Plumber()

house.accept(el)
house.accept(pl)

print()

print(str(house))
print(str(el))
print(str(pl))
