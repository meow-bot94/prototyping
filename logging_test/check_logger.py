import logging
from log_initializer import LogInitializer

LogInitializer('config/log_initializer_config.yaml').init()

logger = logging.getLogger(__name__)

logger.info('info!')
logger.warning('haha')
logger.error('oh no')
