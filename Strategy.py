import types


class Strategy:
    def __init__(self, function=None):

        self.name = "Default Strategy"

        # execute() is being replaced dynamically here
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):
        print("{} is used!\n".format(self.name))


def strategy_one(self):
    print("{} is used to execute method 1\n".format(self.name))


def strategy_two(self):
    print("{} is used to execute method 2\n".format(self.name))


# Default Strategy
s0 = Strategy()
s0.execute()

# Strategy One
s1 = Strategy(strategy_one)
s1.name = "Strategy One"
s1.execute()

# Strategy Two
s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
