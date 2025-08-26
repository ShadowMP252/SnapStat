import logging
import os
import sys

class coloredFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": "\033[37m", # white
        "INFO": "\033[33m", # yellow
        "WARNING": "\033[35m", # purple
        "ERROR": "\033[91m", # red
        "EXCEPTION": "\033[34m", # blue
        "SUCCESS": "\033[32m", # green
        "CRITICAL": "\033[1;31m" # bold red
    }
    RESET = "\033[0m"
    
    def format(self,record):
        log_color = self.COLORS.get(record.levelname ,self.RESET)
        formatted_message = super().format(record)
        colored_message = f"{log_color}{formatted_message}{self.RESET}"
        return colored_message

def init_logger(application):
    logger = logging.getLogger(application)
    logger.setLevel(logging.DEBUG)
    
    log_folder = 'logs'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    
    log_filename = os.path.join(log_folder, f"{application}.log")
    file_handler = logging.FileHandler(log_filename, mode='a')
    file_handler.setLevel(logging.DEBUG)
    
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    
    console_formatter = coloredFormatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

app_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
logger = init_logger(app_name)