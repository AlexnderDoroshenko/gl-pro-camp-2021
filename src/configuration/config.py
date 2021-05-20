"""Module for configuration logic"""
from abc import ABC, ABCMeta, abstractproperty, abstractmethod, abstractclassmethod, abstractstaticmethod

import configparser
import yaml
import json
import os
import local_settings
from src.helpers.validator import Validator


class Config:
    """Main config class"""
    def __init__(self):
        self.env_loader = ConfigFromEnvironment
        self.file_loader = ConfigFromFile
        self.data_loader = ConfigFromData
        self.hierarchy_loader = HierarchyConfigLoader
        conf_path = f"{local_settings.ROOT_DIR}/{os.environ['TARGET']}.json"

    def set_config_variable(self, key: str, value):
        """Method for Config class variable setting

        :param key: Name for Config class attribute.
        :param value: Value for Config class attribute.
        """
        if not hasattr(self, key):
            setattr(self, key, value)
        return self



class ConfigFromEnvironment():
    """Class for providing with environment"""
    def __init__(self):
        self.config = {}

    def get_config(self, var_name: str):
        """Getter method
        :param var_name: Name of the environment variable.
        """
        self.config = os.environ.get(var_name)

    def set_config(self):
        """Setter method.
        Sets attribute for Config class.
        """
        for key, value in self.config.items():
            if not hasattr(Config, key):
                setattr(Config, key, value)


class ConfigFromFile():
    """Class for providing with environment
    Class expected input data in json or yaml file
    """

    def __init__(self):
        self.config = {}
        self.validator = Validator()


    def get_config(self, file_path: str):
        """Getter method
        :param file_path: Name of the file_path with data.
        """
        self.config = self.get_input_from_file(file_path)

    def get_input_from_file(self, file_path: str):
        """
        Takes a file with the yaml or json format and returns a dictionary data.
        :param file_path: Name of the file_path with data.
        """
        if self.validator.file_ext.is_yalm(file_path):
            return self.get_yaml_data(file_path)
        elif self.validator.file_ext.is_json(file_path):
            return self.get_json_data(file_path)
        else:
            raise ValueError("Unsupported file format, supported formats [yaml, json]")

    def get_yaml_data(self, file_path):
        """Method gets data from yaml file
        and returns a dict
        :param file_name: Name of the file_path with data.
        """
        with open(file_path) as f:
            return yaml.safe_load(f)[0]

    def get_json_data(self, file_name):
        """Method gets data from json file
        and returns a dict
        :param file_name: Name of the file with data.
        """
        with open(file_name).read() as f:
            return json.loads(f)

    def set_config(self):
        """Setter method.
        Sets attribute for Config class.
        """
        for key, value in self.config.items():
            if not hasattr(Config, key):
                setattr(Config, key, value)


class ConfigFromData:
    """
    Class for loading the input config data.
        All methods returns a dictionary type data.
        Class expected input data in dict, list, tuple.
    """
    def __init__(self, input_data):
        self.input_data = input_data
        self.config = {}
        self.validator = Validator()

    def get_config(self, input_data: str):
        """Getter method
        :param input_data: Data for config.
        """
        self.config = self.get_input_from_data()

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

    def set_config(self):
        """Setter method.
        Sets attribute for Config class.
        """
        for key, value in self.config.items():
            if not hasattr(Config, key):
                setattr(Config, key, value)


class ConfigIniParser:
    """Class for working with ini files"""
    def __init__(self, file_name: str):
        self.config = configparser.ConfigParser()
        self.config_file_name = file_name
        self.file_path = f"{local_settings.ROOT_DIR}/{self.config_file_name}"
        self.config.read(self.file_path)

    def create_section(self, section_name: str):
        r"""Creates a section in config.

         :param section_name: name of the configuration section.

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


class HierarchyConfigLoader:
    """Class for hierarchy config data loading"""
    def __init__(self, config_set):
        self.config_set = config_set
        self.configuration = {}

    def get_configuration(self):
        for config_item in self.config_set:
            if config_item:
                for key, value in config_item.items():
                    if not key in self.configuration.keys():
                        self.configuration[key] = value
        return self
