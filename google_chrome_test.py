import logging
import pytest
import unittest

from unittest import TestCase
from src.helpers.utils.utils_helper import UtilsHelper
from src.helpers.web.platform_admin.appium_helper import Mobile_testing_helper
from src.helpers.web.platform_admin.signup_helper import SignupHelper
from src.tests.web.base_test import BaseTest


class MobileTesting(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    print("****")
    """
        Test Google chrome basic feature
    """

    def test_google_chrome(self):
        mobile_testing_helper = Mobile_testing_helper()
        signuphelper = SignupHelper()
        utils_helper = UtilsHelper()
        user = utils_helper.get_new_user()
        document = utils_helper.get_upload_documnets()
        address_suggestion = None
        url = None

        # Visit google chrome app
        self.logger.info("****")
        desired_capabilities = mobile_testing_helper.device_desired_capabilities()
        driver = mobile_testing_helper.driver_setup(desired_capabilities)


        # Navigate to home screen
        mobile_testing_helper.navigate_to_google_search()

        # # Visit platform admin page
        # mobile_testing_helper.visit_page()
        #
        # Platform admin sign up
        mobile_testing_helper.signup(
            email=user["email"],
            password=user["password"],
            confirm_password=user["password"]
        )

    def test_qwil_mobile_web_application(self):
        mobile_testing_helper = Mobile_testing_helper()

        # Visit google chrome app
        desired_capabilities = mobile_testing_helper.launch_chrome_device_desired_capabilities()
        driver = mobile_testing_helper.driver_setup(desired_capabilities)

        # Visit Qwil web app
        mobile_testing_helper.visit_qwil_webapp()