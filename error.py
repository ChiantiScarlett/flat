import sys


class RaiseError:
    def __init__(self, message):
        self.raise_error(message)

    def raise_error(self, message):
        print('[*]', message)
        sys.exit(0)
