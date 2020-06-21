import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from base.base_action import BaseAction
from base.base_yaml import yaml_reader

yaml = yaml_reader("webform_text")


class WebformText(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def click_button(self, item):
        item_ele = yaml["button"][item]["attribute"]
        item_position = (By.XPATH, item_ele)
        self.click(item_position)

    def check_text(self, item):
        item_ele = yaml["text"][item]["attribute"]
        item_position = (By.XPATH, item_ele)
        item_text = yaml["text"][item]["content"]
        assert self.get_text(item_position) == item_text




