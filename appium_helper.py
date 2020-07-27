from appium import webdriver
import time
import src.framework.global_config as config
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from src.helpers.utils.mailinator_helper import MailinatorHelper
from src.helpers.utils.utils_helper import UtilsHelper
from src.pages.base_page import BasePage
from src.pages.platform_admin.google_chrome_page import Mobile_testing_page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Mobile_testing_helper():
    mobile_testing_page = Mobile_testing_page()
    mailinator_helper = MailinatorHelper()
    base_page = BasePage()
    # desired_capabilities = None
    driver = None
    touch = None

    # Desired capabilities of the device
    def device_desired_capabilities(self):
        print("******")
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "Xiaomi Redmi Note 7",
            "appPackage": "com.android.chrome",
            "appActivity": "com.google.android.apps.chrome.Main",
            "newCommandTimeout": 120
        }
        # global desired_capabilities
        return desired_capabilities

    def leaforg_desired_capabilities(self):
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "Xiaomi Redmi Note 7",
            "appPackage": "com.testleaf.leaforg",
            "appActivity": "com.testleaf.leaforg.MainActivity",
            "newCommandTimeout": 120
        }
        # global desired_capabilities
        self.wait(5)
        return desired_capabilities

    def launch_chrome_device_desired_capabilities(self):
        print("******")
        desired_capabilities = {
            "platformName": "Android",
            "deviceName": "Xiaomi Redmi Note 7",
            "browserName": "Chrome",
            "chromedriverExecutable": "/Users/Sapthagiri/Downloads/chromedriver 4",
            "udid": "1570ca03",
            "newCommandTimeout": 120
        }
        # global desired_capabilities
        return desired_capabilities

    # Web driver set up
    def driver_setup(self, desired_capabilities):
        global driver
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
        config.DRIVER=driver
        return driver

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

    def visibility_of_element_located(self, selector):
        self.wait()
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(locator=selector)
        )
        #driver.presence_of_element_located(selector)

    # Find the element by ID
    def find_element_id(self, selector):
        self.wait(5)
        print(selector)
        driver.find_element_by_id(selector).click()

    # Find element by Xpath and send value
    def find_xpath_enter_value(self, selector, value):
        self.wait()
        print(selector)
        print(value)
        driver.find_element_by_xpath(selector).send_keys(value)


    # Find element by ID and send value
    def find_element_enter_value(self, selector, value):
        self.wait(5)
        driver.find_element_by_id(selector).send_keys(value)

    # Press Keyevent
    def keycode(self, code):
        self.wait(10)
        print(code)
        driver.press_keycode(code)

    # Implicit wait
    def wait(self, seconds=3):
        time.sleep(seconds)

    # Tap using Touch action
    def tap_action(self, x, y):
        touch = TouchAction()
        touch.tap(x=x, y=y).perform()

    # Long press action using Touch action
    def long_press_action(self, element):
        touch = TouchAction()
        touch.long_press(element).perform()

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
        # driver.find_element_by_id("email-input").send_keys(email)
        driver.find_element_by_xpath("//android.widget.EditText[@bounds='[145,602][935,709]']").click()
        driver.find_element_by_xpath("//android.widget.EditText[@bounds='[145,602][935,709]']").send_keys(email)
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

    """
        TouchAction(driver)   .press(x=540, y=739)   .move_to(x=518, y=1607)   .release()   .perform()
    """
    def create_an_account_in_leafOrg(self,
        email,
        first_name,
        last_name,
        phone_number,
    ):

        self.wait(5)
        self.click_create_account()
        self.wait(6)
        self.enter_first_name(first_name=first_name)
        self.enter_last_name(last_name=last_name)
        self.enter_leaforg_email(email=email)
        self.enter_phone_number(phone_number=phone_number)
        self.click_arrow()
        self.pass_state_name()
        self.wait()


    def select_date_of_birth(self):

        self.click_date_of_birth_dropdown()
        self.wait()
        self.click_year_in_calender()
        self.wait()
        self.swipe_year()
        self.click_selected_year()
        self.select_date()
        self.navigate_month()
        self.desired_day()
        self.click_set()
        self.click_continue_button()
        self.wait(7)

    def swipe_year(self):
        global touch
        touch = TouchAction(driver)
        #touch.long_press(x=230, y=347)
        self.wait()
        for i in range(3):
            self.wait()
            touch.press(x=540, y=739).move_to(x=518, y=1607).release().perform()

    """
        Long press and slide a bar (vertical scroll)
    """
    #touch.long_press(x=540, y=739).move_to(x=518, y=1607).release().perform()



    def click_create_account(self):
        self.wait(10)
        #self.find_element_xpath(selector=self.mobile_testing_page.leafOrg_create_account)
        self.mobile_testing_page.click(self.mobile_testing_page.leafOrg_create_account)

    """
     x=230, y=347
    """
    """
        Multiple actions
        action0 = TouchAction().tap(element)
        action1 = TouchAction().tap(element)
        MultiAction().add(action0).add(action1).perform()
    """
    def enter_first_name(self, first_name):
        touch = TouchAction(driver)
        selector = self.mobile_testing_page.enter_first_name
        self.wait()
        value = first_name
        # name_selector = driver.find_element_by_xpath("//android.widget.EditText[@bounds='[110,313][995,371]']")
        #self.wait(3)
        driver.find_element_by_xpath("//android.widget.EditText[@bounds='[110,313][995,371]']").send_keys(first_name)
        #self.find_xpath_enter_value(selector, value)
        #touch.long_press(x=169, y=347, duration=10000)
        # self.wait(3)
        # touch.long_press(name_selector, duration=10000).perform()
        # self.wait(10)
        # touch.tap(x=333, y=239).perform()
        # self.wait(3)
        # touch.tap(x=254, y=239).perform()
        # self.wait(15)

    def enter_last_name(self, last_name):
        self.wait(5)
        # touch = TouchAction(driver)
        # name_selector = driver.find_element_by_xpath("//android.widget.EditText[@bounds='[110,440][995,495]']")
        # touch.long_press(name_selector, duration=10000).perform()
        # self.wait(10)
        # touch.tap(x=150, y=362).perform()
        selector = self.mobile_testing_page.enter_last_name
        value = last_name
        self.find_xpath_enter_value(selector, value)

    def enter_leaforg_email(self, email):
        self.wait(5)
        selector = self.mobile_testing_page.enter_email
        value = email
        self.find_xpath_enter_value(selector, value)

    def enter_phone_number(self, phone_number):
        #self.wait()
        selector = self.mobile_testing_page.enter_phone_number
        value = phone_number
        self.find_xpath_enter_value(selector, value)

    def click_arrow(self):
        self.wait()
        self.find_element_xpath(selector=self.mobile_testing_page.state_arrow)

    def pass_state_name(self):
        self.wait(5)
        self.find_element_xpath(selector=self.mobile_testing_page.state_name)

    def click_date_of_birth_dropdown(self):
        self.wait(10)
        self.find_element_xpath(selector=self.mobile_testing_page.dob_dropdown)

    def click_year_in_calender(self):
        self.wait(10)
        self.find_element_id(selector=self.mobile_testing_page.year_in_calender)

    """
        TouchAction(driver)   .press()   .move_to()   .release()   .perform()
    """
    def touch_driver(self):
        global touch
        touch = TouchAction(driver)
        return touch

    def click_selected_year(self):
        self.wait(10)
        self.find_element_xpath(selector=self.mobile_testing_page.selected_year)

    def select_date(self):
        self.wait(10)
        self.find_element_id(selector=self.mobile_testing_page.date)

    def click_set(self):
        self.wait(10)
        self.find_element_id(selector=self.mobile_testing_page.set_button)

    def click_continue_button(self):
        self.wait(5)
        self.find_element_xpath(selector=self.mobile_testing_page.continue_button)

    def enter_continue_button(self):
        self.wait(5)
        self.find_element_xpath(selector=self.mobile_testing_page.press_continue_button)

    def license_information(self, license):
        self.wait(5)
        self.add_license(license=license)
        self.click_license_exp_date()
        self.click_set()
        self.enter_continue_button()

    def add_license(self, license):
        selector = self.mobile_testing_page.license_number
        print(license)
        value1 = "125125124"
        value2 = license
        self.find_xpath_enter_value(selector, value1)
        touch.long_press(x=164, y=470, duration=10000).perform()
        #self.wait(5)
        touch.tap(x=470, y=343).perform()
        self.wait()
        driver.find_element_by_xpath(selector).clear()
        self.find_xpath_enter_value(selector, value2)



    def click_license_exp_date(self):
        self.wait(10)
        self.find_element_xpath(selector=self.mobile_testing_page.license_exp_date)

    def participants_information(self, participant_id, mentor_name, group_name):
        self.wait(5)
        self.add_particpant_id(participant_id=participant_id)
        self.select_join_date()
        self.click_set()
        self.type_mentors_name(mentor_name=mentor_name)
        self.group_name(group_name=group_name)

        self.click_submit_registration()
        self.click_ok_button()
        self.click_submit_registration()

    def add_particpant_id(self, participant_id):
        self.wait()
        print("*****CHECKPOINT******")
        #driver.find_element_by_xpath("//android.widget.EditText[@bounds='[110,432][995,487]']").click().send_keys(1241241)
        # print("*****ELEMENT*****", element)
        # element.clear()
        # element.send_keys("12512513")
        #driver.find_element_by_xpath("//android.widget.EditText[@bounds='[110,432][995,487]']").send_keys(participant_id)
        # selector = self.mobile_testing_page.enter_participant_id
        # value = participant_id
        # self.find_xpath_enter_value(selector, value)
        touch.long_press(x=174, y=451, duration=10000).perform()
        self.wait(10)
        touch.tap(x=117, y=347).perform()
        self.wait(3)

    def select_join_date(self):
        self.wait(10)
        self.find_element_xpath(selector=self.mobile_testing_page.enter_join_date)

    def type_mentors_name(self, mentor_name):
        self.wait(5)
        selector = self.mobile_testing_page.enter_mentor_name
        value = mentor_name
        self.find_xpath_enter_value(selector, value)

    def group_name(self, group_name):
        self.wait(5)
        selector = self.mobile_testing_page.enter_group_name
        value = group_name
        self.find_xpath_enter_value(selector, value)

    def click_submit_registration(self):
        self.wait()
        self.find_element_xpath(selector=self.mobile_testing_page.submit_registration)

    def click_ok_button(self):
        self.wait(5)
        self.find_element_xpath(selector=self.mobile_testing_page.ok_button)

    def validate_login_page(self):
        self.validate_title()

    def validate_title(self):
        self.visibility_of_element_located(selector=self.mobile_testing_page.leafOrg_create_account)
        #driver.find_element_by_id(selector)
        #self.base_page.wait_for_presence(selector)


    def navigate_month(self):
        self.wait(5)
        for i in range(2):
            self.wait(5)
            self.find_element_id(selector=self.mobile_testing_page.next)

    def desired_day(self):
        self.wait(10)
        self.find_element_xpath(selector=self.mobile_testing_page.desired_date)


    def visit_qwil_webapp(self):
        self.enter_qwil_url()

    def enter_qwil_url(self):
        url = "https://app-dev.builds.qwil.co/platform/signup"
        self.url_navigation(url=url)

    def url_navigation(self, url):
        driver.get(url)
        self.wait(10)
        print("*******")
        #driver.find_element_by_xpath("//android.widget.EditText[@bounds='[145,602][935,709]']").click()
        #driver.find_element_by_id("email-input").send_keys("Sapthagiri")
        driver.find_element_by_id("email-input").click()