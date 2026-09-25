import os
import logging
from datetime import datetime

# Logger folder creation
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Log file creation
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def get_logger(name: str = __name__) -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
        )

        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    log = get_logger(__name__)
    log.info("Logger test message - log started")