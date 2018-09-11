# class Borg:
#     _shared_state  = {}
#     def __init__(self):
#         self.__dict__ = self._shared_state
#
#
# class Singleton(Borg):
#     def __init__(self, **kwargs):
#         Borg.__init__(self)
#         self._shared_state.update(kwargs)
#
#     def __str__(self):
#         return str(self._shared_state)
#
# x = Singleton(HTTP = "Hyper Text Transfer Protocol", AK = "Akshay Kulkarni")
# print(x)
# y = Singleton(SNMP = "Simple Network Management Protocol")
# print(y)
# -----------------------------------------------

# class MyMeta(type):
#     """
#     __call__ function doesn't return anything
#     """
#     def __call__(cls, *args, **kwargs):
#         print("meta!")
#         return super(MyMeta, cls).__call__(*args, **kwargs)
#
# class MyClass(metaclass=MyMeta):
#     def __init__(self):
#         print("class!")
#
#     @classmethod
#     def get_instance(self):
#         return MyClass()
#
# if __name__ == '__main__':
#     c = MyClass.get_instance()
#     print(c)
# -----------------------------------------------
# BEST METHOD BELOW

def Singleton(myClass):
    instances = {}
    def getInstance(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstance

@Singleton
class TestClass(object):
    pass

x = TestClass()
# -----------------------------------------------
