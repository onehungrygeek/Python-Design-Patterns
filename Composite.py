class Component(object):
    def __init__(self, *args, **kwargs):
        pass

    def componentFunction(self):
        pass


class Child(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]

    def componentFunction(self):
        print("{}".format(self.name))


class Composite(Component):
    def __init__(self, *args, **kwargs):
        Component.__init__(self, *args, **kwargs)
        self.name = args[0]
        self.children = []

    def appendChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def componentFunction(self):
        print("{}".format(self.name))
        for i in self.children:
            i.componentFunction()


subMenu1 = Composite("subMenu1")

subMenu1_1 = Child("subMenu1_1")
subMenu1_2 = Child("subMenu1_2")

subMenu1.appendChild(subMenu1_1)
subMenu1.appendChild(subMenu1_2)

topMenu = Composite("topMenu")
subMenu2 = Child("subMenu2")
topMenu.appendChild(subMenu1)
topMenu.appendChild(subMenu2)

topMenu.componentFunction()
