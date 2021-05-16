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
        """Abstract method for config setting"""
        raise NotImplemented


class Config(AbstractConfig):
    """Main config class"""
    def __init__(self, input_data: str):
        self.input_data = input_data
        self.data_loader = ConfigLoader(self.input_data)

    def set_config(self, key: str, value):
        """Method for config setting"""
        self.__setattr__(name=key, value=value)


class ConfigLoader:
    """Class for loading the input config data
    all methods returns a dictionary type data."""
    def __init__(self, input_data: str):
        self.input_data = input_data

    def is_file(self):
        """Method check is input data a file."""
        if os.path.isfile(self.input_data):
            return "file"

    def is_file_yaml(self):
        """Method check is input data a yaml file."""
        return self.input_data.endswith(".yaml")

    def is_file_json(self):
        """Method check is input data a json file.."""
        return self.input_data.endswith(".json")

    def get_input_data(self):
        """
        Method with loader logic.
        Takes a file with the yaml or json format and returns a dictionary.
        If data is dictionary returns it as is.
        If data is correct tuple or list, returns data converted in dictionary.
        """
        if self.is_file():
            if self.is_file_yaml():
                return self.get_yaml_data()
            elif self.is_file_json():
                return self.get_json_data()
            else:
                raise ValueError("Unsupported file format, supported formats [yaml, json]")
        elif isinstance(self.input_data, (dict, tuple, list)):
            if isinstance(self.input_data, dict):
                return self.input_data
            if isinstance(self.input_data, tuple):
                if sum((x for x in self.input_data if len(x) != 2)) == 0:
                    return {x[0]: x[1] for x in self.input_data if len(x) == 2}
                else:
                    raise ValueError("Wrong tuple format, each index should have two nested index")
            if isinstance(self.input_data, list):
                if sum((x for x in self.input_data if len(x) != 2)) == 0:
                    return {x[0]: x[1] for x in self.input_data if len(x) == 2}
                else:
                    raise ValueError("Wrong list format, each index should have two nested index")
            else:
                raise ValueError("Unsupported data type, class supports types [dict, tuple, list]")

    def get_yaml_data(self):
        """Method gets data from yaml file
        and returns a dict"""
        with open(self.input_data) as f:
            return yaml.safe_load(f)[0]

    def get_json_data(self):
        """Method gets data from json file
        and returns a dict"""
        with open(self.input_data).read() as f:
            return json.loads(f)