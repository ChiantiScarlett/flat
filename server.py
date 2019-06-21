import dropbox
import json
import sys


class _Dropbox:
    def __init__(self, keys):
        self._key = keys[0]

    def initialize_server(self):
        """
        Initialize connection
        """
        pass

    def upload_file(self):
        """
        Upload single file to Dropbox server.
        """
        pass

    def download(self):
        """
        Download folder or file from Dropbox server.
        """
        pass

    def upload_folder(self):
        """
        Upload folder and its contents to Dropbox server.
        """
        pass


class ServerLinker:
    """
    Read settings.json file and load appropriate server class
    """

    def __init__(self):
        self._servers = ['Dropbox']  # possible servers

        # Read settings.json file
        with open('settings.json', 'r') as fp:
            self.settings = json.loads(fp.read())

        # Validate SERVER_TYPE:
        if self.settings['SERVER_TYPE'] not in self._servers:
            self.raise_error(
                'Invalid server type < {} >'
                .format(self.settings['SERVER_TYPE']))
        elif self.settings['SERVER_TYPE'] == 'Dropbox':
            self.server = _Dropbox(self.settings['KEYS'])

    def raise_error(self, message):
        print('[*]', message)
        sys.exit(0)
