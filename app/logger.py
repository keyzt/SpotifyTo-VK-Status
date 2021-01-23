import sys
import logging
from loguru import (logger)


SAVE_LOGS_IN_FILE = False
SERIALIZE_LOGS = True


config = {
    "handlers": [
        {
        	"sink": sys.stdout,
        	"format": "<green>{time:YYYY-MM-DD HH:mm:ss}</green> - {message}"
        }
    ]
}

logger.configure(**config)

if SAVE_LOGS_IN_FILE:
	filename = "app.json" if SERIALIZE_LOGS else "app.log"
	logger.add(filename, serialize=SERIALIZE_LOGS, rotation="10 MB")


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


logging.basicConfig(
	handlers=[InterceptHandler()], 
	level=logging.INFO
)
