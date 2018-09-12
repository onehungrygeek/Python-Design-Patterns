# Elf, Dwarf and Human
from ObserverPattern import Observable, Obeserver

class Elf:
    name = 'Zorin'

    def speakA(self):
        print("Speaking Elvish...")


class Dwarf:
    name = 'Ragnaf'

    def speakB(self):
        print("Speaking Dwarvish...")


class Human:
    name = 'Gandalf'

    def speakC(self):
        print("Speaking English...")


# ------------ADAPTER DESIGN PATTERN------------
# BELONGS TO 1
# NO: NO ADAPTER BELOW
# if __name__ == '__main__':
#     minions = [Elf(), Dwarf(), Human()]
#
#     for minion in minions:
#         if isinstance(minion, Elf):
#             minion.speakA()
#         elif isinstance(minion, Dwarf):
#             minion.speakB()
#         else:
#             minion.speakC()

# BETTER: RESPECTIVE ADAPTER BELOW
# class ElfAdapter:
#     def __init__(self, elf):
#         self.elf = elf
#
#     def call_me(self):
#         self.elf.speakA()
#
# class DwarfAdapter:
#     def __init__(self, dwarf):
#         self.dwarf = dwarf
#
#     def call_me(self):
#         self.dwarf.speakB()
#
# class HumanAdapter:
#     def __init__(self, human):
#         self.human = human
#
#     def call_me(self):
#         self.human.speakC()
#
# if __name__ == '__main__':
#     minions = [ElfAdapter(Elf()),
#                 DwarfAdapter(Dwarf()),
#                 HumanAdapter(Human())]
#
#     for minion in minions:
#         minion.call_me()

# BEST: GENERAL ADAPTER BELOW
# class MinionAdapter:
#     _initialised = False
#
#     def __init__(self, minion, **kwargs):
#         self.minion = minion
#
#         for key, value in kwargs.items():
#             func = getattr(self.minion, value)
#             self.__setattr__(key, func)
#
#         self._initialised = True
#
#     def __getattr__(self, attr):
#         return getattr(self.minion, attr)
#
#     def __setattr__(self, key, value):
#         # Set attributes normally during initialisation
#         if not self._initialised:
#             super().__setattr__(key, value)
#         # Set attributes on minion after initialisation
#         else:
#             setattr(self.minion, key, value)


# if __name__ == '__main__':
#     minionAdapters = [
#                         MinionAdapter(Elf(), speak='speakA'),
#                         MinionAdapter(Dwarf(), speak='speakB'),
#                         MinionAdapter(Human(), speak='speakC')
#                         ]
#
#     for adapter in minionAdapters:
#         adapter.speak()
#     # COOL THING ABOUT ABOVE ADAPTER
#     elf_adapter = minionAdapters[0]
#     print()
#     print(f'Name from Adapter: {elf_adapter.name}')
#     print(f'Name from Minion: {elf_adapter.minion.name}')
#     print()
#     elf_adapter.name = 'Brethrek'
#     print(f'Name from Adapter: {elf_adapter.name}')
#     print(f'Name from Minion: {elf_adapter.minion.name}')

# ------------FACADE DESIGN PATTERN------------
# class MinionFacade:
#     minionAdapters = None
#
#     @classmethod
#     def createMinions(cls):
#         print("Creating minions...")
#         cls.minionAdapters = [
#             MinionAdapter(Elf(), speak='speakA'),
#             MinionAdapter(Dwarf(), speak='speakB'),
#             MinionAdapter(Human(), speak='speakC')
#         ]
#
#     @classmethod
#     def summonMinions(cls):
#         print("Summoning minions...")
#         for adapter in cls.minionAdapters:
#             adapter.speak()
#
#
# if __name__ == '__main__':
#     MinionFacade.createMinions()
#     MinionFacade.summonMinions()

# ------------OBSERVER DESIGN PATTERN------------
class MinionAdapter(Observable):
    _initialised = False

    def __init__(self, minion, **kwargs):
        super().__init__()
        self.minion = minion

        for key, value in kwargs.items():
            func = getattr(self.minion, value)
            self.__setattr__(key, func)

        self._initialised = True

    def __getattr__(self, attr):
        return getattr(self.minion, attr)

    def __setattr__(self, key, value):
        if not self._initialised:
            super().__setattr__(key, value)
        else:
            setattr(self.minion, key, value)
            self.notifyObserver(key=key, value=value)


class MinionFacade:
    minionAdapters = None

    @classmethod
    def createMinions(cls):
        print("Creating minions...")
        cls.minionAdapters = [
            MinionAdapter(Elf(), speak='speakA'),
            MinionAdapter(Dwarf(), speak='speakB'),
            MinionAdapter(Human(), speak='speakC'),
        ]

    @classmethod
    def summonMinions(cls):
        print("Summoning minions...")
        for minion in cls.minionAdapters:
            minion.speak()

    @classmethod
    def monitorMinions(cls, observer):
        cls.minionAdapters[0].addObserver(observer)
        print("Added an oberver to the Elves!")

    @classmethod
    def changeElfName(cls, name):
        print("Changing the Elf's name...")
        cls.minionAdapters[0].name = name
        print("Elf's name changed successfully to %s" %
              cls.minionAdapters[0].name)


class EvilOverlord(Obeserver):
    def update(self, obj, *args, **kwargs):
        print("Overlord alerted!")
        print(f'Object: {obj}, Args: {args}, Kwargs: {kwargs}')


if __name__ == '__main__':
    overlord = EvilOverlord()

    MinionFacade.createMinions()
    MinionFacade.summonMinions()
    MinionFacade.monitorMinions(overlord)
    MinionFacade.changeElfName('Berzerk')
