"""Module for configuration logic"""
from abc import ABC, ABCMeta, abstractproperty, abstractmethod, abstractclassmethod, abstractstaticmethod

import configparser
import yaml
import json
import os


class AbstractConfig(ABC):
    """Abstract class for config implementation"""
    @abstractmethod
    def set_config(self, key: str, value):
        raise NotImplemented

class Config(AbstractConfig):
    """Main config class"""
    def __init__(self, input_data):
        self.input_data = input_data
        self.data_loader = ConfigLoader(self.input_data)

    def set_config(self, key: str, value):
        self.__setattr__(name=key, value=value)


class ConfigLoader:
    def __init__(self, file: str):
        self.file = file

    def get_input_data(self):
        if os.path.isfile(self.file):
            if self.file.endswith(".yaml"):
                return self.get_yaml_data()
            if self.file.endswith(".json"):
                return self.get_json_data()
            else:
                raise ValueError("Unsupported file extension")
        else:
            raise FileNotFoundError


    def get_yaml_data(self):
        with open(self.file) as f:
            return yaml.safe_load(f)

    def get_json_data(self):
        with open(self.file).read() as f:
            return json.loads(f)