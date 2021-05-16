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

