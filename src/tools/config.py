from pathlib import Path
import json
from configparser import ConfigParser


def parse(config_file_path):
    if Path(config_file_path).suffix == '.json':
        with open(config_file_path, 'r') as file:
            config = json.load(file)
    else:
        config = ConfigParser()
        config.read(config_file_path)
    return config['mysql']
