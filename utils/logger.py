import logging
import os

def get_logger():
    logger = logging.getLogger("api_logger")

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # Create logs folder if not exists
        if not os.path.exists("logs"):
            os.makedirs("logs")

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File handler
        file_handler = logging.FileHandler("logs/test.log")
        file_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger