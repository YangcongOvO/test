import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_yaml import yaml_reader
from selenium.webdriver.support.ui import Select

yaml = yaml_reader("webform_selector")


class WebformSelector(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_button(self, item):
        item_ele = yaml["button"][item]["attribute"]
        item_position = (By.XPATH, item_ele)
        self.click(item_position)

    def check_options(self, item):
        item_ele = yaml["selector"][item]["attribute"]
        options_list = Select(self.driver.find_element(By.XPATH, item_ele)).options
        options = list(option.text for option in options_list)
        item_value = yaml["selector"][item]["value"]
        assert options == item_value

    def select_option(self, item, value):
        item_ele = yaml["selector"][item]["attribute"]
        Select(self.driver.find_element(By.XPATH, item_ele)).select_by_value(value)

    def selected_option(self, item):
        item_ele = yaml["selector"][item]["attribute"]
        selected_option = Select(self.driver.find_element(By.XPATH, item_ele)).first_selected_option.text
        return selected_option

    def check_checkbox(self, item, value):
        for i in value:
            item_ele = yaml[item][i]
            item_position = (By.XPATH, item_ele)
            self.click(item_position)

    def agree_unselected(self):
        item_position = ("Id", "edit-actions-submit")
        agree_unselected = self.has_attribute(item_position, "disabled")
        return agree_unselected

