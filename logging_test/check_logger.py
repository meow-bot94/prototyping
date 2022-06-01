import logging
from log_initializer import LogInitializer
from logging_test.singleton_log_collator import SingletonLogCollator

LogInitializer('config/log_initializer_config.yaml').init()

logger = logging.getLogger(__name__)

logger.info('info!')
logger.warning('haha')
logger.error('oh no')

print('collated logs:')
print(SingletonLogCollator().get_logs())
