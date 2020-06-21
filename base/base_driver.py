from selenium import webdriver
from .base_yaml import yaml_reader
from selenium.webdriver.common.keys import Keys
yaml = yaml_reader("driver")

def en_driver():
    en_driver = webdriver.Chrome()
    # en_driver.get("https://collectionastellascom.ast001.acsitefactory.com/en/form/register-form")
    en_driver.get(yaml["driver en"]["URL"])
    # en_driver.get('https://stage.astellas.com/jp/en/partnering/register-form')
    # en_driver.switch_to_alert().sendKeys("astellas" + Keys.TAB + "Astellas@123")
    # en_driver.switch_to_alert().accept()
    # en_driver.get("https://astellas:Astellas@123@ci-jp.ast002.com/jp/en/partnering/register-form")
    return en_driver

def golobal_driver():
    golobal_driver = webdriver.Chrome()
    # golobal_driver.get("https://collectionastellascom.ast001.acsitefactory.com/en/form/register-form")
    # golobal_driver.get("https://astellas:Astellas@123@collectionastellascom.test-ast001.acsitefactory.com/partnering/register-form/")
    golobal_driver.get(yaml["driver gl"]["URL"])
    return golobal_driver

def ja_driver():
    ja_driver = webdriver.Chrome()
    # golobal_driver.get("https://collectionastellascom.ast001.acsitefactory.com/en/form/register-form")
    # ja_driver.get("https://astellas:Astellas@123@collectionastellascomjp.test-ast001.acsitefactory.com/jp/ja/form/register-form/")
    ja_driver.get(yaml["driver ja"]["URL"])
    return ja_driver
