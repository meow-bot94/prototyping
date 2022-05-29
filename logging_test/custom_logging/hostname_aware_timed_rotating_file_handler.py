import socket
import pathlib
import logging
import logging.handlers


class HostnameAwareTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(self, filename, *args, **kwargs):
        filename = pathlib.Path(filename)
        hostname = socket.gethostname()
        file_parent = filename.parent
        custom_filename = f'{hostname}_{filename.name}'
        custom_file_path = file_parent / custom_filename
        file_parent.mkdir(exist_ok=True, parents=True)
        super().__init__(custom_file_path, *args, **kwargs)
