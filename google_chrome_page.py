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

    leafOrg_create_account = (By.XPATH, "//android.view.View[@text='Create an Account']")
    enter_first_name = "//android.widget.EditText[@bounds='[110,313][995,371]']"
    enter_last_name = "//android.widget.EditText[@bounds='[110,440][995,495]']"
    enter_email = "//android.widget.EditText[@bounds='[110,566][995,621]']"
    enter_phone_number = "//android.widget.EditText[@bounds='[203,693][995,748]']"
    state_arrow = "//android.widget.Image[@text='arrow forward']"
    state_name = "//android.view.View[@text='TamilNadu']"
    dob_dropdown = "//android.widget.Spinner[@bounds='[343,946][786,1017]']"
    year_in_calender = "android:id/date_picker_header_year"
    selected_year = "//android.widget.TextView[@text='1996']"
    date = "android:id/date_picker_header_date"
    set_button = "android:id/button1"
    continue_button = "//android.widget.Button[@text='CONTINUE']"
    license_number = "//android.widget.EditText[@bounds='[110,432][995,487]']"
    license_exp_date = "//android.widget.Spinner[@bounds='[338,558][781,630]']"

    enter_participant_id = "//android.widget.EditText[@bounds='[110,432][995,487]']"
    enter_mentor_name = "//android.widget.EditText[@bounds='[110,701][995,756]']"
    enter_group_name = "//android.widget.EditText[@bounds='[110,828][995,883]']"
    enter_join_date = "//android.widget.Spinner[@bounds='[283,558][726,630]']"
    submit_registration = "//android.widget.Button[@text='SUBMIT REGISTRATION']"

    ok_button = "//android.widget.Button[@text='OK']"

    leaforg_title = "//android.view.View[@text='LeafOrg']"
    next = "android:id/next"
    desired_date = "//android.view.View[@text='1']"
    press_continue_button = "//android.widget.Button[@bounds='[404,701][676,773]']"