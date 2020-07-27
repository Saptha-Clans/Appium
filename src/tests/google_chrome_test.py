import logging
import pytest
import unittest

from unittest import TestCase
from src.helpers.utils.utils_helper import UtilsHelper
from src.helpers.web.platform_admin.google_chrome_helper import Mobile_testing_helper
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
        mobile_testing_helper.driver_setup(desired_capabilities)

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

        # Fill the personal information
        signuphelper.enter_personal_information(user=user, url=url)

        # Fill the compamy information
        signuphelper.enter_company_information(
            user=user, address_suggestion=address_suggestion
        )

        # Upload the W9 tax and article documents
        signuphelper.upload_documents(document=document, url=url)

        # Add directors page
        signuphelper.add_directors_page(url=url)

        # Enter the contractor underwriting detials
        signuphelper.enter_contractor_under_writing_details(user=user, document=document)

        # Enter the bank account information
        signuphelper.enter_bank_account_information(user=user)
