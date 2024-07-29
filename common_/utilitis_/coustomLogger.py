import logging
from datetime import date
import os

from pathlib import Path
import inspect


def get_root_dir_name():
    command = "Path(__file__).absolute()"
    while True:
        rootDir = str(eval(command))
        if rootDir.split(sep="\\")[-1] == "AmazonTestEnv":
            return rootDir
        else:
            command += ".parent"


def logger(level, message, fileName=os.path.join(get_root_dir_name(), '_logs_', f'log_{date.today()}.log')):
    logging.basicConfig(level=logging.INFO, filename=fileName, filemode="a",
                        format="%(asctime)-12s %(levelname)s %(message)s",
                        datefmt="%d-%m-%Y %H:%M:%S")
    print(os.path.join(get_root_dir_name(), '_logs_', f'log_{date.today()}.log'))
    if level == "INFO":
        logging.info(message)
        return
    if level == "DEBUG":
        logging.debug(message)
        return
    if level == "WARNING":
        logging.warning(message)
        return
    if level == "ERROR":
        logging.error(message)
        return
    if level == "CRITICAL":
        logging.critical(message)
        return


def logg(function):
    def wrapper(*args):
        logger("INFO", f"Calling < {inspect.stack()[0][3]}> method")
        function(*args)
        logger("INFO", f"Finished<{inspect.stack([0][3])}> method")

    return wrapper
