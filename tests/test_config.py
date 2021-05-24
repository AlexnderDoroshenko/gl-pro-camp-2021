"""Test module for unit testing src/configuration/config.py"""

import pytest
import allure
import os

from src.configuration.config import *


@allure.feature("ConfigFromEnvironment")
class TestConfigFromEnv:
    """Tests for ConfigFromEnvironment class"""
    @allure.story("Get value from env variable.")
    @pytest.mark.parametrize(argnames="key, value", argvalues=[("test_get_var", "test_get_value")], ids=["positive"])
    def test_get_env_config_value(self, key, value):
        with allure.step("Setting a new env variable."):
            os.environ[key] = value
        with allure.step("Getting a new env variable."):
            value_from_function = ConfigFromEnvironment().set_config_value_from_env(var_name=key).config[key]
        with allure.step("Comparing values."):
            assert value == value_from_function, f"Test value : {value}, but function returns : {value_from_function}"

    @allure.story("Set value to env variable.")
    @pytest.mark.parametrize(argnames="key, value", argvalues=[("test_set_var", "test_set_value")], ids=["positive"])
    def test_set_env_config_value(self, key, value):
        with allure.step("Setting a new env variable."):
            ConfigFromEnvironment().set_env_config_value(var_name=key, value=value)
        with allure.step("Comparing values."):
            assert os.environ.get(key)

    @allure.story("Sets variables to config.")
    @pytest.mark.parametrize(argnames="key, value", argvalues=[("test_set_config", "test_set_config_value")], ids=["positive"])
    def test_set_config(self, key, value):
        with allure.step("Setting an env variables."):
            os.environ[key] = value
        with allure.step("Setting config from environment."):
            conf_obj = Config().env_loader().set_config_value_from_env(key).set_config()
        with allure.step("Comparing values."):
            assert Config().__getattribute__(key) == value


class TestConfigFromFile:
    """Tests for ConfigFromEnvironment class"""
    @allure.story("Get value from env variable.")
    @pytest.mark.parametrize(argnames="key, value", argvalues=[("test_get_var", "test_get_value")], ids=["positive"])
    def test_get_env_config_value(self, key, value):
        with allure.step("Setting a new env variable."):
            os.environ[key] = value
        with allure.step("Getting a new env variable."):
            value_from_function = ConfigFromEnvironment().set_config_value_from_env(var_name=key).config[key]
        with allure.step("Comparing values."):
            assert value == value_from_function, f"Test value : {value}, but function returns : {value_from_function}"

    @allure.story("Set value to env variable.")
    @pytest.mark.parametrize(argnames="key, value", argvalues=[("test_set_var", "test_set_value")], ids=["positive"])
    def test_set_env_config_value(self, key, value):
        with allure.step("Setting a new env variable."):
            ConfigFromEnvironment().set_env_config_value(var_name=key, value=value)
        with allure.step("Comparing values."):
            assert os.environ.get(key)

    @allure.story("Sets variables to config.")
    @pytest.mark.parametrize(argnames="key, value", argvalues=[("test_set_config", "test_set_config_value")], ids=["positive"])
    def test_set_config(self, key, value):
        with allure.step("Setting an env variables."):
            os.environ[key] = value
        with allure.step("Getting an env variables."):
            conf_obj = Config().env_loader().set_config_value_from_env(key).set_config()
        with allure.step("Comparing values."):
            assert Config().__getattribute__(key) == value
