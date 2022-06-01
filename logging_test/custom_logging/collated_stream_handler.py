import logging
from logging_test.singleton_log_collator import SingletonLogCollator


class CollatedStreamHandler(logging.StreamHandler):
    def __init__(self):
        output = SingletonLogCollator().logs
        super().__init__(output)
