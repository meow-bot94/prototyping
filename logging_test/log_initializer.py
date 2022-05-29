import logging
import logging.config
import datetime
import pytz
import pathlib
import yaml
from typing import Union


class LogInitializer:
    def __init__(
            self,
            config_path: Union[str, pathlib.Path],
    ):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)

    def init(self):
        self._format_timezone()
        self.init_logger_config()

    def _format_timezone(self):
        timezone = pytz.timezone(self.config['timezone'])
        logging.Formatter.converter = lambda *x: datetime.datetime.now(timezone).timetuple()

    def init_logger_config(self):
        logger_config_path = self.config['logger_config_path']
        with open(logger_config_path, 'r') as f:
            logger_config = yaml.safe_load(f)
        logging.config.dictConfig(logger_config)
