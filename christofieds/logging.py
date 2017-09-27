
import logging
from logging import DEBUG, INFO

log_initialized = False

def init_log():
    if not log_initialized:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG) 
        global log_initialized
        log_initialized = True

def args_string(message, *args):        
    return str(message) + " " + " ".join((str(arg) for arg in args))

def log(message, *args):
    init_log()
    logging.log(INFO, args_string(message, *args))

def log_debug(message, *args):
    init_log()
    logging.log(DEBUG, args_string(message, *args))

 
