"""
utils_logger.py

Reusable logger setup for Python projects.
"""

import logging

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler - writes logs to project.log
file_handler = logging.FileHandler("project.log")
file_handler.setLevel(logging.DEBUG)

# Console handler - writes logs to console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Log format
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Attach formatters to handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Attach handlers to logger (avoid duplicates)
if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

# Quick test (runs only if you run this file directly)
if __name__ == "__main__":
    logger.info("Logger is working!")