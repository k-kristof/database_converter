from configparser import ConfigParser

def parse(config_file_path):
    config = ConfigParser()
    config.read(config_file_path)
    return config