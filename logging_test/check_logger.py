import logging
from log_initializer import LogInitializer
from logging_test.singleton_log_collator import SingletonLogCollator
from logging_test.verbose_module.verbosely_printing import verbose_print
from logging_test.silent_module.silently_printing import silent_print
from logging_test.silent_config_module.silent_config_printing import silent_config_print

LogInitializer('config/log_initializer_config.yaml').init()

logger = logging.getLogger(__name__)

logger.info('info!')
logger.warning('haha')
logger.error('oh no')

print('check modules')
verbose_print()
silent_print()
silent_config_print()

print('collated logs:')
print(SingletonLogCollator().get_logs())
