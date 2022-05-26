import time
from duplicate_process_terminator import DuplicateProcessTerminator
from termination_manager import TerminationManager

process_mgr = DuplicateProcessTerminator()
print(f'process name: {process_mgr.process_name}')
process_mgr.check_and_kill_duplicate_process()

with TerminationManager():
    print('sleeping...')
    time.sleep(10)

print('end')
