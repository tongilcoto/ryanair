import configparser

def before_all(context):

    context.config = configparser.ConfigParser()
    context.config.read("defaults.ini")

