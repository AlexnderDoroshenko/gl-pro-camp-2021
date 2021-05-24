"""Module for validators implementation"""

import os


class Validator:
    """
    Main validators class, maybe it should be some kind of a factory.

    """
    def __init__(self):
        self.os = OsValidator()
        self.file_ext = FileExtValidator()


class OsValidator:
    """Os entities validations class"""
    def __init__(self):
        self.os = os
        self.path = os.path

    def is_file(self, file_path: str):
        """
        Returns true if file exist in the path from arg.

        :param file_path: full path to the file.
        :return: boolean
        """
        return self.path.isfile(file_path)

    def is_dir(self, file_path: str):
        """
        Returns true if dir exist in the path from arg.

        :param file_path: full path to the directory.
        :return: boolean
        """
        return self.path.isdir(file_path)


class FileExtValidator():
    """File ext validations class"""
    @staticmethod
    def is_json(file_name: str):
        """
        Returns true if file extension is json.

        :param file_name: Name of the file with extension.
        :return: boolean
        """
        return file_name.endswith(".json")

    @staticmethod
    def is_yalm(file_name: str):
        """
        Returns true if file extension is yaml.

        :param file_name: Name of the file with extension.
        :return: boolean
        """
        return file_name.endswith(".yaml")

    @staticmethod
    def is_env(file_name: str):
        """
        Returns true if file extension is env.

        :param file_name: Name of the file with extension.
        :return: boolean
        """
        return file_name.endswith(".env")

    @staticmethod
    def is_ini(file_name: str):
        """
        Returns true if file extension is ini.

        :param file_name: Name of the file with extension.
        :return: boolean
        """
        return file_name.endswith(".ini")





