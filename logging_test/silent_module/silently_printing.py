import logging


logger = logging.getLogger(__name__)


def silent_print():
    logger.info('i am silent')
