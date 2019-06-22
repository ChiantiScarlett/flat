import sys

DIRECTION_DL_OPTS = ['dl', 'd', 'download']
DIRECTION_DL_KEY = "download"
DIRECTION_UL_OPTS = ['ul', 'u', 'upload']
DIRECTION_UL_KEY = "upload"


class RaiseError:
    def __init__(self, message):
        self.raise_error(message)

    def raise_error(self, message):
        print('[*]', message)
        sys.exit(0)
