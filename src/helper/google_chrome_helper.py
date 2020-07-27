from appium import webdriver
import time

from selenium.webdriver.common.by import By

from src.helpers.utils.mailinator_helper import MailinatorHelper
from src.helpers.utils.utils_helper import UtilsHelper
from src.pages.base_page import BasePage
from src.pages.platform_admin.google_chrome_page import Mobile_testing_page


class Mobile_testing_helper():
    mobile_testing_page = Mobile_testing_page()
    mailinator_helper = MailinatorHelper()
    base_page = BasePage()
    # desired_capabilities = None
    driver = None

    # Desired capabilities of the device
    def device_desired_capabilities(self):
        print("******")
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "Xiaomi Redmi Note 7",
            "appPackage": "com.android.chrome",
            "appActivity": "com.google.android.apps.chrome.Main"
        }
        # global desired_capabilities
        return desired_capabilities

    # Web driver set up
    def driver_setup(self, desired_capabilities):
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)


    # execute script mobile actions {go, search, send, next, done, previous}
    def execute_action(self, action):
        self.wait(5)
        driver.execute_script('mobile: performEditorAction', {'action': action})

    # Find element by class
    def find_element_by_class(self, element, button_element=None):
        self.wait(5)
        button = driver.find_element_by_class_name(element)
        driver.set_value(button, button_element)

    # Find the element by xpath
    def find_element_xpath(self, selector):
        self.wait(5)
        driver.find_element_by_xpath(selector).click()

    # Find the element by ID
    def find_element_id(self, selector):
        self.wait(5)
        print(selector)
        driver.find_element_by_id(selector).click()

    # Find element by Xpath and send value
    def find_xpath_enter_value(self, selector, value):
        self.wait(5)
        element = driver.find_element_by_xpath(selector).send_keys(value)
        self.wait(5)
        # element.send_keys(value)

    # Find element by ID and send value
    def find_element_enter_value(self, selector, value):
        self.wait(5)
        driver.find_element_by_id(selector).send_keys(value)
        self.wait(10)
        # element.send_keys("https://app-dev.builds.qwil.co/platform/signup")

    # Press Keyevent
    def keycode(self, code):
        self.wait(10)
        print(code)
        driver.press_keycode(code)

    # Implicit wait
    def wait(self, seconds=3):
        time.sleep(seconds)

    def navigate_to_google_search(self):
        self.click_accept_and_continue()
        self.click_next_button()
        self.press_no_thanks()
        driver.get("https://app-dev.builds.qwil.co/platform/signup")

        # self.wait(10)
        # self.sign_in_google()

    def click_accept_and_continue(self):
        self.wait(10)
        self.find_element_id(selector=self.mobile_testing_page.accept_and_continue)
        # driver.find_element_by_id("com.android.chrome:id/terms_accept").click()

    def click_next_button(self):
        self.wait(10)
        self.find_element_id(selector=self.mobile_testing_page.next_button)
        # driver.find_element_by_id("com.android.chrome:id/next_button").click()

    def sign_in_google(self):
        self.wait(10)
        driver.find_element_id(selector=self.mobile_testing_page.sign_in)
        # driver.find_element_by_id("com.android.chrome:id/positive_button").click()

    def press_no_thanks(self):
        self.wait(10)
        self.find_element_id(selector=self.mobile_testing_page.no_thanks)
        # driver.find_element_by_id("com.android.chrome:id/negative_button").click()

    def visit_page(self):
        self.wait(10)
        value = "https://app-dev.builds.qwil.co/platform/signup"
        self.enter_search_text(value=value)

    def enter_search_text(self, value):
        selector = self.mobile_testing_page.google_search
        self.find_element_enter_value(value=value, selector=selector)
        # self.base_page.type(text=value, selector=selector)
        self.click_search()
        self.wait(40)

    def click_search(self):
        self.execute_action(action="go")

    def signup(self, email, password, confirm_password, url=None, submit=True):
        #self.mobile_testing_page.type(selector=self.mobile_testing_page.email, text=email)
        #driver.find_element_by_id("email-input").send_keys(email)
        self.enter_email(email=email)
        self.wait(10)
        self.enter_password(password=password)
        self.wait(20)
        self.enter_confirm_password(confirm_password=confirm_password)

    #     if submit:
    #         self.click_signup_button()
    #         token = self.mailinator_helper.get_qwil_token_from_mailinator_email(
    #             email=email, subject="E-mail verification requested"
    #         )
    #         self.confirm_signup_email(token=token, url=url)
    #         UtilsHelper().wait(seconds=5)
    #
    # def confirm_signup_email(self, token, url=None):
    #     self.signup_page.open_url(
    #         uri=self.signup_page.APP_URL
    #         + "/platform/signup/personal-information?token=%s" % token
    #     )

    def enter_email(self, email):
        self.wait(10)
        print(email)
        selector = self.mobile_testing_page.email
        print(selector)
        self.find_element_enter_value(value=email, selector=selector)

    def enter_password(self, password):
        self.wait(10)
        selector = self.mobile_testing_page.password
        self.find_element_enter_value(value=password, selector=selector)

    def enter_confirm_password(self, confirm_password):
        self.wait(10)
        selector = self.mobile_testing_page.confirm_password
        self.find_element_enter_value(value=confirm_password, selector=selector)

    def find_class_name(self, selector):
        driver.find_element_by_class_name(selector).click()

    def click_signup_button(self):
        self.wait(10)
        self.find_class_name(selector=self.mobile_testing_page.sign_up)
