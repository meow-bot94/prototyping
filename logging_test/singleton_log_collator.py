import io


class SingletonLogCollator:
    __logs = io.StringIO()

    def __init__(self):
        self._logs = SingletonLogCollator.__logs

    @property
    def logs(self):
        return self._logs

    def get_logs(self):
        return self.logs.getvalue()
