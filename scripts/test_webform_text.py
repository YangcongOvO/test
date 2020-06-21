import os, sys
sys.path.append(os.getcwd())
from base.base_driver import golobal_driver, en_driver, ja_driver
from page.webform_page_text import WebformText
from page.webform_selector import WebformSelector
from page.webform_input import WebformInput
import allure
import pytest

text = ["title", "body", "company", "contact title", "opportunity title",
        "opportunity subtitle", "area title", "attachment title",
        "attachment description", "submission title", "submission subtitle",
        "submission content"]
selector = ["deal_type", "opportunity_type", "current_development"]
input_box = ["company", "URL", "country", "address1", "address2", "postal_code",
             "first_name", "last_name", "email", "phone", "fax", "stage", "total",
             "closing", "opportunity", "primary", "secondary", "brand_name",
             "action", "description", "launch_year", "territory"]
empty_error = ["company", "country", "address1", "first_name", "last_name",
               "email", "phone", "opportunity"]
type_error = ["URL", "postal_code", "email", "phone", "fax"]

class TestWebformText:

    def setup_class(self):
        self.driver_golobal = golobal_driver()
        self.page_gl_text = WebformText(self.driver_golobal)
        self.page_gl_selector = WebformSelector(self.driver_golobal)
        self.page_gl_input = WebformInput(self.driver_golobal)
        self.driver_en = en_driver()
        self.page_en_text = WebformText(self.driver_en)
        self.page_en_selector = WebformSelector(self.driver_en)
        self.page_en_input = WebformInput(self.driver_en)
        self.driver_ja = ja_driver()
        self.page_ja_text = WebformText(self.driver_ja)
        self.page_ja_selector = WebformSelector(self.driver_ja)
        self.page_ja_input = WebformInput(self.driver_ja)

    def teardown_class(self):
        self.driver_golobal.quit()
        self.driver_en.quit()
        self.driver_ja.quit()


    @pytest.mark.parametrize("item", ["agree_notice"])
    def test_gl_click_agree_notice(self, item):
        self.page_gl_text.click_button(item + " gl")

    @pytest.mark.parametrize("item", ["agree_notice"])
    def test_en_click_agree_notice(self, item):
        self.page_en_text.click_button(item + " en")

    @pytest.mark.parametrize("item", ["agree_notice"])
    def test_ja_click_agree_notice(self, item):
        self.page_ja_text.click_button(item + " ja")

    @pytest.mark.parametrize("item", text)
    def test_gl_check_text(self, item):
        self.page_gl_text.check_text(item + " gl")

    @pytest.mark.parametrize("item", text)
    def test_en_check_text(self, item):
        self.page_en_text.check_text(item + " en")

    @pytest.mark.parametrize("item", text)
    def test_ja_check_text(self, item):
        self.page_ja_text.check_text(item + " ja")

    @pytest.mark.parametrize("item", selector)
    def test_gl_check_options(self, item):
        self.page_gl_selector.check_options(item + " gl")

    @pytest.mark.parametrize("item", selector)
    def test_en_check_options(self, item):
        self.page_en_selector.check_options(item + " en")

    @pytest.mark.parametrize("item", selector)
    def test_ja_check_options(self, item):
        self.page_ja_selector.check_options(item + " ja")

    @pytest.mark.parametrize("item", input_box)
    def test_gl_check_placeholder(self, item):
        self.page_gl_input.check_placeholder(item + " gl")

    @pytest.mark.parametrize("item", input_box)
    def test_en_check_placeholder(self, item):
        self.page_en_input.check_placeholder(item + " en")

    @pytest.mark.parametrize("item", input_box)
    def test_ja_check_placeholder(self, item):
        self.page_ja_input.check_placeholder(item + " ja")

    @pytest.mark.parametrize("item", input_box)
    def test_gl_check_maxlength(self, item):
        self.page_gl_input.check_maxlength(item + " gl")

    @pytest.mark.parametrize("item", input_box)
    def test_en_check_maxlength(self, item):
        self.page_en_input.check_maxlength(item + " en")

    @pytest.mark.parametrize("item", input_box)
    def test_ja_check_maxlength(self, item):
        self.page_ja_input.check_maxlength(item + " ja")

    @pytest.mark.parametrize("item", empty_error)
    def test_gl_empty_error_message(self, item):
        self.page_gl_input.check_empty_message(item + " gl")

    @pytest.mark.parametrize("item", empty_error)
    def test_en_empty_error_message(self, item):
        self.page_en_input.check_empty_message(item + " en")

    @pytest.mark.parametrize("item", empty_error)
    def test_ja_empty_error_message(self, item):
        self.page_ja_input.check_empty_message(item + " ja")

    @pytest.mark.parametrize("item", type_error)
    def test_gl_type_error_message(self, item):
        self.page_gl_input.check_empty_message(item + " gl")

    @pytest.mark.parametrize("item", type_error)
    def test_en_type_error_message(self, item):
        self.page_en_input.check_empty_message(item + " en")

    @pytest.mark.parametrize("item", type_error)
    def test_ja_type_error_message(self, item):
        self.page_ja_input.check_empty_message(item + " ja")