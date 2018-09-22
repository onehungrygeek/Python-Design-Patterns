class Handler:  # Abstract Handler
    def __init__(self, successor):
        self._successor = successor  # Define who is the next handler

    def handle(self, request):
        handled = self._handle(request)

        # If handled, stop. Otherwise, keep going.
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass!')


class DefaultHandler(Handler):
    def _handle(self, request):  # No condition since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True


class ConcreteHandler(Handler):
    def _handle(self, request):
        if 0 < request <= 10:  # Handling condition
            print("Request {} handled in ConcreteHandler".format(request))
            return True


class Client:
    def __init__(self):
        # Create handlers and use them in a any sequence
        # DefaultHandler has no successor here
        self.handler = ConcreteHandler(DefaultHandler(None))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


c = Client()
requests = [2, 5, 9, 30, 6]
c.delegate(requests)
