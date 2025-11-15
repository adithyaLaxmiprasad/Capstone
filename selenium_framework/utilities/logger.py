import logging
import os
from datetime import datetime

class Logger:

    @staticmethod
    def get_logger():
        # Create logs directory if not exists
        logs_dir = os.path.join(os.getcwd(), "logs")
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Log file name
        log_file = os.path.join(logs_dir, f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)

        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        # Avoid duplicate handlers
        if not logger.handlers:
            logger.addHandler(file_handler)

        return logger
