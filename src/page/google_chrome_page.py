from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class Mobile_testing_page(BasePage):
    accept_and_continue = "com.android.chrome:id/terms_accept"
    next_button = "com.android.chrome:id/next_button"
    sign_in = "com.android.chrome:id/positive_button"
    no_thanks = "com.android.chrome:id/negative_button"
    google_search = "com.android.chrome:id/search_box_text"
    email = "email-input"
    #email = (MobileBy.ID, "email-input")
    password = "password-input"
    confirm_password = "confirm-password-input"
    sign_up = "android.widget.Button"
