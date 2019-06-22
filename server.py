import dropbox
import json
from core import RaiseError
from core import DIRECTION_DL_KEY, DIRECTION_UL_KEY


class _Dropbox:
    def __init__(self, keys):
        self._key = keys[0]
        self.initialize_server()

    def initialize_server(self):
        """
        Initialize connection
        """
        self.API = dropbox.Dropbox(self._key)

    def upload_file(self, local_path, remote_path):
        """
        Upload single file to Dropbox server.
        """
        with open(local_path, 'rb') as fp:
            self.API.files_upload(fp.read(), remote_path,
                                  mode=dropbox.files.WriteMode('overwrite'))

    def download_file(self, local_path, server_path):
        """
        Download folder or file from Dropbox server.
        """
        self.API.files_download_to_file(local_path, server_path)


class ServerLinker:
    """
    Read settings.json file and load appropriate server class
    """

    def __init__(self, direction, remote_path, local_path):
        self._servers = ['Dropbox']  # possible servers
        self.direction = direction
        self.remote_path = remote_path
        self.local_path = local_path

        # Read settings.json file
        with open('settings.json', 'r') as fp:
            self.settings = json.loads(fp.read())

        # Validate SERVER_TYPE and initialize server:
        if self.settings['SERVER_TYPE'] not in self._servers:
            RaiseError(
                'Invalid server type < {} >'
                .format(self.settings['SERVER_TYPE']))
        elif self.settings['SERVER_TYPE'] == 'Dropbox':
            self.server = _Dropbox(self.settings['KEYS'])

    def run(self):
        if self.direction == DIRECTION_DL_KEY:
            self.download(self.local_path, self.remote_path)

        elif self.direction == DIRECTION_UL_KEY:
            self.upload(self.local_path, self.remote_path)

    def upload(self, local_path, remote_path):
        self.server.upload_file(local_path, remote_path)

    def download(self, local_path, remote_path):
        self.server.download_file(local_path, remote_path)
