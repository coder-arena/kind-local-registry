import os

from distutils.util import strtobool

# Server
SERVER_DEBUG = strtobool(os.getenv('SERVER_DEBUG', 'False'))
