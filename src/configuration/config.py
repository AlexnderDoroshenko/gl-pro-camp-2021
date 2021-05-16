"""Module for configuration logic"""
from abc import ABC, ABCMeta, abstractproperty, abstractmethod, abstractclassmethod, abstractstaticmethod

import configparser
import yaml
import json
import os
import settings


class Config:
    """Main config class"""

    def set_config_class_variable(self, key: str, value):
        """Method for Config class variable setting"""
        self.__setattr__(key, value)

    def set_config_class_variable_from_env(self, env_key:str):
        """Method for Config class variable setting from os environment"""
        self.set_config_class_variable(env_key, os.environ[env_key])

    def set_config_class_variables_from_data(self, input_data):
        """Method for Config class variables setting from data input"""
        dict_from_data = ConfigLoader(input_data=input_data).get_input_data()
        for key, value in dict_from_data:
            self.set_config_class_variable(key=key, value=value)


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
            return self.get_input_from_file()
        elif isinstance(self.input_data, (dict, tuple, list)):
            return self.get_input_from_data()

    def get_input_from_file(self):
        """
        Takes a file with the yaml or json format and returns a dictionary data.
        """
        if self.is_file_yaml():
            return self.get_yaml_data()
        elif self.is_file_json():
            return self.get_json_data()
        else:
            raise ValueError("Unsupported file format, supported formats [yaml, json]")

    def get_input_from_data(self):
        """
        Takes a correct data and returns a dictionary.
        """
        if isinstance(self.input_data, dict):
            if sum((value for key, value in self.input_data.items() if not isinstance(value, dict)))== 0:
                return self.input_data
        if isinstance(self.input_data, tuple):
            if sum((x for x in self.input_data if len(x) != 3)) == 0:
                return {x[0]: x[1] for x in self.input_data}
            else:
                raise ValueError("Wrong tuple format, each index should have three nested index")
        if isinstance(self.input_data, list):
            if sum((x for x in self.input_data if len(x) != 3)) == 0:
                return {x[0]: x[1] for x in self.input_data}
            else:
                raise ValueError("Wrong list format, each index should have three nested index")

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


class ConfigIniParser:
    """Class for working with ini files"""
    def __init__(self, file_name: str):
        self.config = configparser.ConfigParser()
        self.config_file_name = file_name
        self.file_path = f"{settings.ROOT_DIR}/{self.config_file_name}"
        self.config.read(self.file_path)

    def create_section(self, section_name: str):
        """Method creates a section in config"""
        self.config[section_name] = {}
        self.save_config_file()

    def create_section_values(self, section_name: str, values_dict: dict):
        """Method creates a section values in config"""
        if section_name not in self.config.sections():
            self.config.add_section(section_name)
        for key, value in values_dict.items():
            self.config.set(section_name, key, value)
        self.save_config_file()

    def save_config_file(self):
        """Method saves config"""
        with open(self.file_path, 'w') as configfile:
            self.config.write(configfile)

    def get_config_value(self, section: str, key: str):
        """
        Method get a value from config by section option(key)
        """
        return self.config.get(section=section, option=key)




