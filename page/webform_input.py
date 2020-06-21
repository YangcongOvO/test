import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_yaml import yaml_reader
import re

yaml = yaml_reader("webform_input")
data_yaml = yaml_reader("webform_data")


class WebformInput(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_button(self, item):
        item_ele = yaml["button"][item]["attribute"]
        item_position = (By.XPATH, item_ele)
        self.click(item_position)

    def check_placeholder(self, item):
        item_ele = yaml["input_box"][item]["attribute"]
        item_position = (By.XPATH, item_ele)
        item_placeholder = yaml["input_box"][item]["placeholder"]
        assert self.get_placeholder(item_position) == item_placeholder

    def check_maxlength(self, item):
        item_ele = yaml["input_box"][item]["attribute"]
        item_func = re.findall(r"id='(.*)'", item_ele)[0]
        item_position = ("Id", item_func)
        item_maxlength = yaml["input_box"][item]["maxlength"]
        assert int(self.get_attribute(item_position, "maxlength")) == item_maxlength

    def check_empty_message(self, item):
        item_ele = yaml["input_box"][item]["attribute"]
        item_func = re.findall(r"id='(.*)'", item_ele)[0]
        item_position = ("Id", item_func)
        item_error_message = yaml["input_box"][item]["error_message"]
        if item_error_message == "None":
            assert self.get_attribute(item_position, "data-webform-required-error") is None
        else:
            assert self.get_attribute(item_position, "data-webform-required-error") == item_error_message

    def check_type_message(self, item):
        item_ele = yaml["input_box"][item]["attribute"]
        item_func = re.findall(r"id='(.*)'", item_ele)[0]
        item_position = ("Id", item_func)
        item_error_message = yaml["input_box"][item]["error_message"]
        if item_error_message == "None":
            assert self.get_attribute(item_position, "data-webform-pattern-error") is None
        else:
            assert self.get_attribute(item_position, "data-webform-pattern-error") == item_error_message

    def fill_text(self, item, value):
        item_ele = yaml["input_box"][item]["attribute"]
        item_position = (By.XPATH, item_ele)
        self.input_text(item_position, value)
