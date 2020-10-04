import logging


SAVE_TO_FILE = False

consoleFormatter = logging.StreamHandler()
fileFormatter = logging.FileHandler(filename="app.log", encoding="utf-8")

fileFormatter.setFormatter(
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
)

logging_handlers = [consoleFormatter, fileFormatter] if SAVE_TO_FILE else [consoleFormatter] 

logging.basicConfig(
    format='%(asctime)s - %(message)s',
    level=logging.INFO,
    handlers=logging_handlers,
    datefmt='%Y-%m-%d %H:%M:%S'
)


logger = logging.getLogger('app')
