import base64
import logging
import os

import pytest
import unittest
import time
from unittest import TestCase

from src.helpers.utils.mailinator_helper import MailinatorHelper
from src.helpers.utils.utils_helper import UtilsHelper
from src.helpers.web.platform_admin.appium_helper import Mobile_testing_helper


class MobileTesting(unittest.TestCase):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    print("****")
    mailinator_helper = MailinatorHelper()

    """
        Create a account in LeafOrg test 
    """

    def test_leaforg(self):
        mobile_testing_helper = Mobile_testing_helper()
        utils_helper = UtilsHelper()
        user = utils_helper.get_new_user()

        # Visit LeaffOrg
        self.logger.info("****")
        desired_capabilities = mobile_testing_helper.leaforg_desired_capabilities()
        driver = mobile_testing_helper.driver_setup(desired_capabilities)


        # Start recording video
        driver.start_recording_screen()

        # Create an account
        mobile_testing_helper.create_an_account_in_leafOrg(
            email=utils_helper.get_random_string(size=10) + "@gmail.com",
            first_name=user["first_name"],
            last_name=user["last_name"],
            phone_number="999-999-9999"
        )

        # Select date of birth with co-ordinates
        mobile_testing_helper.select_date_of_birth()

        # Drivers license information
        mobile_testing_helper.license_information(
            license="A9999999"
        )

        # Participants ID
        mobile_testing_helper.participants_information(
            participant_id="54321672",
            mentor_name="Sapthagiri",
            group_name="Executors"
        )

        # Verify login page after sign up
        mobile_testing_helper.validate_login_page()

        # Save the video
        video_rawData = driver.stop_recording_screen()

        # Create file_name
        video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

        # Create file_path
        file_path = os.path.join("/Users/Sapthagiri/Workspace/appium-mobile-testing/videoRecording/", video_name+".mp4")

        # Convert the base64 file to media file
        with open(file_path, "wb") as vd:
            vd.write(base64.b64decode(video_rawData))

        # # Hide Keyboard
        # driver.hide_keyboard()
        #
        # # Screenshot
        # driver.save_screenshot("/Users/Sapthagiri/Workspace/appium-mobile-testing/videoRecording/", video_name+".png")