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

    def set_config(self, key: str, value):
        self.__setattr__(name=key, value=value)

