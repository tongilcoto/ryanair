from behave import *
import logging
import configparser
from inspect import getsourcefile
from os.path import abspath, join
from pathlib import Path

def before_all(context):

    # os.getcwd() is getting PyCharm Directory!!!!!
    # Workaround is ...
    currentscript = abspath(getsourcefile(lambda:0))
    currentdir = str(Path(currentscript).parent)
    logfile = join(currentdir, 'billing.log')
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -  %(message)s', filename= logfile)

    context.config = configparser.ConfigParser()
    context.config.read("defaults.ini")

