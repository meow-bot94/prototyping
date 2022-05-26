import signal
import sys
import time
import psutil
import os
import setproctitle
from pathlib import Path
import subprocess


process_name = Path(__file__).name
setproctitle.setproctitle(process_name)
print(setproctitle.getproctitle())


def sigint_handler(signum, frame):
    print('received SIGTERM')
    raise KeyboardInterrupt('haha')


signal.signal(signal.SIGTERM, sigint_handler)


print(psutil.Process())
self_pid = psutil.Process().pid
for proc in psutil.process_iter(['pid', 'name', 'username']):
    if proc.info['name'] == 'python.exe' and proc.info['pid'] != self_pid:
        print(f'killing {proc.info}')
        os.kill(proc.info['pid'], signal.SIGTERM)
        # signal.pidfd_send_signal(proc.info['pid'], signal.SIGTERM)
print('sleeping...')
time.sleep(10)
print('end')
