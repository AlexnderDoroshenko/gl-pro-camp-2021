"""Module for validators implementation"""

import os


class Validator:
    def __init__(self):
        self.os = OsValidator()
        self.file_ext = FileExtValidator()

class OsValidator:
    """Os entities validations"""
    def __init__(self):
        self.os = os
        self.path = os.path

    def is_file(self, file_path: str):
        return self.path.isfile(file_path)

    def is_dir(self, file_path: str):
        return self.path.isdir(file_path)


class FileExtValidator():

    def is_json(self, file_name: str):
        return file_name.endswith(".json")

    def is_yalm(self, file_name: str):
        return file_name.endswith(".yaml")

    def is_env(self, file_name: str):
        return file_name.endswith(".env")

    def is_ini(self, file_name: str):
        return file_name.endswith(".ini")





