import signal
import logging
# Referenced from here: https://stackoverflow.com/questions/18499497/how-to-process-sigterm-signal-gracefully


logger = logging.getLogger(__name__)


class AbortedException(InterruptedError):
    pass


class TerminationManager:
    killed = False

    def _handler(self, signum, frame):
        logging.error("Received SIGINT or SIGTERM!")
        print('aborting!')
        self.killed = True

    def __enter__(self):
        self.old_sigint = signal.signal(signal.SIGINT, self._handler)
        self.old_sigterm = signal.signal(signal.SIGTERM, self._handler)

    def __exit__(self, type, value, traceback):
        if self.killed:
            raise AbortedException('terminated')
        signal.signal(signal.SIGINT, self.old_sigint)
        signal.signal(signal.SIGTERM, self.old_sigterm)
