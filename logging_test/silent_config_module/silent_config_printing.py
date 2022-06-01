import logging


logger = logging.getLogger(__name__)


def silent_config_print():
    logger.info('i am silent due to config')
