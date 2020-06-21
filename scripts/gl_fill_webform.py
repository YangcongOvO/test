import os, sys
import time

sys.path.append(os.getcwd())
from base.base_driver import golobal_driver, en_driver, ja_driver
from page.webform_input import WebformInput
from page.webform_selector import WebformSelector
from base.base_yaml import yaml_reader, txt_written, txt_over_written
from selenium.webdriver.common.by import By


driver_yaml = yaml_reader("driver")
yaml = yaml_reader("webform_data")[driver_yaml["webform_data"]]
cdp_list = driver_yaml["condition"]["cdp"]
dt_list = driver_yaml["condition"]["dt"]
aoi_list = driver_yaml["condition"]["aoi"]
upload_file = driver_yaml["file"]


class FillWebform():

    def __init__(self):
        self.driver_en = golobal_driver()
        self.page_en_input = WebformInput(self.driver_en)
        self.page_en_selector = WebformSelector(self.driver_en)

    def select_en_dt(self, value):
        self.page_en_selector.select_option("deal_type en", value)

    def select_en_ot(self, value):
        self.page_en_selector.select_option("opportunity_type en", value)

    def select_en_cdp(self, value):
        self.page_en_selector.select_option("current_development en", value)

    def select_en_noa(self, value):
        self.page_en_selector.select_option("number_of_assets en", value)

    def select_en_checkbox(self, *args):
        for value in args:
            self.page_en_selector.check_checkbox("checkbox en", value)

    def fill_input_box(self):
        for key, value in yaml["input_box"].items():
            self.page_en_input.fill_text(key, value)
            time.sleep(0.5)

    def fill_selected_box(self):
        if self.page_en_selector.selected_option("deal_type en") == \
                "Equity/Debt finance with board observer right and 8weeks prior to closing date":
            for key, value in yaml["precondition_selected"].items():
                self.page_en_input.fill_text(key, value)
        else:
            pass

    def upload_attachment(self):
        self.page_en_input.input_text((By.XPATH, "//input[@type='file']"), upload_file)


if __name__ == '__main__':
    success = 0
    fail = 0
    file_name = "log/" + time.strftime("Gl%Y_%m_%d_%H_%M_%S", time.localtime())
    os.mkdir(file_name)
    FillWebform = FillWebform()
    FillWebform.page_en_input.click_button("agree_notice en")
    current_URL = FillWebform.driver_en.current_url
    for aoi in aoi_list:
        for cdp in cdp_list:
            for dt in dt_list:
                FillWebform.driver_en.get(current_URL)
                FillWebform.upload_attachment()
                FillWebform.fill_input_box()
                # DT
                FillWebform.select_en_dt(dt)
                FillWebform.select_en_ot("A")
                # CDP
                FillWebform.select_en_cdp(cdp)
                FillWebform.select_en_noa("A")
                # AOI "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"
                FillWebform.select_en_checkbox(aoi)
                FillWebform.fill_selected_box()
                # FillWebform.page_en_input.click_button("agree en")
                if FillWebform.page_en_selector.agree_unselected():
                    FillWebform.page_en_selector.click_button("agree en")
                FillWebform.page_en_input.click_button("submit en")
                time.sleep(2)
                if FillWebform.driver_en.current_url != current_URL:
                    result = "Submit successfully"
                    success += 1
                    success_log = "'cdp': %s \n'dt': %s\n'aoi': %s\n" % (cdp, dt, aoi)
                    txt_written(success_log, file_name + "/success_log")
                else:
                    result = "Submit failed"
                    fail += 1
                    fail_log = "'cdp': %s \n'dt': %s\n'aoi': %s\n" % (cdp, dt, aoi)
                    txt_written(fail_log, file_name + "/fail_log")
                sum = "'success': %s \n'fail': %s\n" % (success, fail)
                txt_over_written(sum, file_name + "/sum")
    FillWebform.driver_en.quit()
