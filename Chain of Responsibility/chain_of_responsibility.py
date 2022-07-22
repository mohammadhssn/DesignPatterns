"""
    Behavioral => (They focus on how classes and objects are supposed to work with each other
    and how they behave with each other.)

        Chain of Responsibility:
            When our program is going to receive a different type of information and return a different type of response
             we can use the chain of responsibility design pattern.
"""
from abc import ABC, abstractmethod


class AbstractHandler(ABC):
    def __init__(self, successor):
        self.successor = successor

    def handle(self, request):
        handled = self.process_request(request)
        if not handled:
            self.successor.handle(request)

    @abstractmethod
    def process_request(self, request):
        pass


# ---------------------------------------------------------------------------------------------------------------------
class HandlerOne(AbstractHandler):

    def process_request(self, request):
        if 0 < request <= 10:
            print(f'Handler One is processing this request... {request}')
            return True


class HandlerTow(AbstractHandler):

    def process_request(self, request):
        if 10 < request <= 20:
            print(f'Handler Tow is processing this request... {request}')
            return True


class DefaultHandler(AbstractHandler):

    def process_request(self, request):
        print(f'This request has no handler so default handler is processing this request... {request}')
        return True


# ---------------------------------------------------------------------------------------------------------------------

class Client:
    def __init__(self):
        self.handler = HandlerOne(HandlerTow(DefaultHandler(None)))

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


# ---------------------------------------------------------------------------------------------------------------------

requests = [2, 10, 32, 16]

client = Client()
client.delegate(requests)
