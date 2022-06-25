"""
    Set of logger utility functions that can be used by any module.
"""

import logging
from pathlib import Path


def setup_logger(logging_file):
    """
    Setup logger.

    Args:
        log_file [str]: path to log file
    """

    # set the path for the logger
    logger_path = Path(logging_file)

    # create a new directory if it doesn't exist
    logger_path.parent.mkdir(parents=True, exist_ok=True)

    # create a new logger
    logger = logging.getLogger(__name__)

    # set the logger level
    logger.setLevel(logging.DEBUG)

    # create a file handler for the logger
    file_handler = logging.FileHandler(logging_file, mode="w")

    # set the formatter for the logger
    formatter = logging.Formatter(
        "%(asctime)s : %(levelname)s : %(name)s : %(message)s"
    )

    # set the formatter for the file handler
    file_handler.setFormatter(formatter)

    # add the file handler to the logger
    logger.addHandler(file_handler)

    # add info to the logger
    logger.info("Finished logger configuration!")

    return logger
