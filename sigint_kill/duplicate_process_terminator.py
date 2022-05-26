import __main__
import signal
import sys
import time
import psutil
import os
import setproctitle
from pathlib import Path
import subprocess


class DuplicateProcessTerminator:
    def __init__(self):
        self._main_path = self._get_main_path()
        self.process_name = Path(self._main_path).stem
        self.process = psutil.Process()
        setproctitle.setproctitle(self.process_name)

    def _get_main_path(self):
        if hasattr(__main__, '__file__'):
            return os.path.abspath(__main__.__file__)
        return os.path.abspath(__file__)

    def get_process_id(self):
        return self.process.pid

    def get_process_info(self):
        return self.process

    def check_and_kill_duplicate_process(self):
        for proc in psutil.process_iter(['pid', 'name', 'username']):
            if proc.info['name'] == self.process_name and proc.info['pid'] != self.get_process_id():
                print(f'killing {proc.info}')
                os.kill(proc.info['pid'], signal.SIGINT)
            elif proc.info['name'] == 'python.exe' and proc.info['pid'] != self.get_process_id():  # use self.process_name in linux; windows issues
                print(proc)
                print(f'killing {proc.info}')
                os.kill(proc.info['pid'], signal.CTRL_C_EVENT)

