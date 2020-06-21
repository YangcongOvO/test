import os, sys
sys.path.append(os.getcwd())
from selenium.webdriver.support.wait import WebDriverWait
import time


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def my_find_element(self, loc):
        function_by = loc[0]
        element_value = loc[1]
        return WebDriverWait(self.driver, 2, 0.2).until(lambda x: x.find_element(function_by, element_value))

    def my_find_elements(self, loc):
        function_by = loc[0]
        element_value = loc[1]
        return WebDriverWait(self.driver, 2, 0.2).until(lambda x: x.find_elements(function_by, element_value))

    def click(self, loc):
        self.my_find_element(loc).click()
        time.sleep(0.5)

    def input_text(self, loc, text):
        self.my_find_element(loc).send_keys(text)
        time.sleep(0.5)

    def input_texts(self, loc, text, multi=1):
        text *= multi
        self.input_text(loc, text)

    def get_text(self,loc):
        text_elemtnt = self.my_find_element(loc)
        text_content = text_elemtnt.text
        return text_content

    def get_placeholder(self,loc):
        placeholder_elemtnt = self.my_find_element(loc)
        placeholder_text = placeholder_elemtnt.get_attribute("placeholder")
        return placeholder_text

    def get_js_text(self, loc):
        text_element = "return document.getElementBy%s('%s').value" % (loc[0], loc[1])
        text_content = self.driver.execute_script(text_element)
        return text_content

    def get_attribute(self, ele, att):
        element = "return document.getElementBy%s('%s').getAttribute('%s')" % (ele[0], ele[1], att)
        attribute = self.driver.execute_script(element)
        return attribute

    def has_attribute(self, ele, att):
        element = "return document.getElementBy%s('%s').hasAttribute('%s')" % (ele[0], ele[1], att)
        attribute = self.driver.execute_script(element)
        return attribute

    def js_text_change(self, loc, text):
        text_element = "document.getElementBy%s('%s').value='%s'" % (loc[0], loc[1], text)
        self.driver.execute_script(text_element)



