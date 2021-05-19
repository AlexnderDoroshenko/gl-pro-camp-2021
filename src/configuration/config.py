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
        """Method for Config class variable setting

        :param key: sets an attribute name for Config class.
        :param value: sets a value for attribute.
        """

        self.__setattr__(key, value)
        return self

    def set_config_class_variable_from_env(self, env_key:str):
        """Method for Config class variable setting from os environment"""
        self.set_config_class_variable(env_key, os.environ.get(env_key))
        return self

    def set_config_class_variables_from_data(self, input_data):
        """Method for Config class variables setting from data input"""
        dict_from_data = ConfigLoader(input_data=input_data).get_input_data()
        for key, value in dict_from_data:
            self.set_config_class_variable(key=key, value=value)
        return self


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
            if sum((x for x in self.input_data if len(x) != 2)) == 0:
                return {x[0]: x[1] for x in self.input_data}
            else:
                raise ValueError("Wrong tuple format, each index should have two nested index")
        if isinstance(self.input_data, list):
            if sum((x for x in self.input_data if len(x) != 2)) == 0:
                return {x[0]: x[1] for x in self.input_data}
            else:
                raise ValueError("Wrong list format, each index should have two nested index")

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
        r"""Creates a section in config.

         :param section: name of the configuration section.
         :param key: name of the configuration section option.

         :return: : config.ConfigParser
         """

        self.config[section_name] = {}
        self.save_config_file()

        return self

    def create_section_values(self, section_name: str, values_dict: dict):
        r"""Creates a section values in config.

         :param section_name: name of the configuration section.
         :param values_dict: key values dictionary.

         :return: : config.ConfigParser
         """

        if section_name not in self.config.sections():
            self.config.add_section(section_name)
        for key, value in values_dict.items():
            self.config.set(section_name, key, value)
        self.save_config_file()

        return self

    def save_config_file(self):
        r"""Saves the config file.

         :return: : config.ConfigParser
         """

        with open(self.file_path, 'w') as configfile:
            self.config.write(configfile)

        return self

    def get_config_value(self, section: str, key: str):
        r"""Gets a value from config by section option(key).

         :param section: name of the configuration section.
         :param key: name of the configuration section option.

         :return: : section option value
         """

        return self.config.get(section=section, option=key)




