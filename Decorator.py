from functools import wraps


def makeBlink(function):
    """
    MakeBlink Doc
    """
    @wraps(function)
    def decorator():
        ret = function()
        return "<blink>" + ret + "</blink>"

    return decorator


@makeBlink
def hello_world():
    """
    HelloWorld Doc
    """
    return "Hello, world!"


print(hello_world())
print(hello_world.__name__)
print(hello_world.__doc__)
