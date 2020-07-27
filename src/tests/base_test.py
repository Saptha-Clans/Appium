import json
import logging
import os
from unittest import TestCase
from selenium import webdriver
from src.framework.env_data import EnvData
from src.framework.browser_config import browser_config
import src.framework.global_config as config
from selenium.webdriver.chrome.options import Options

# from sauceclient import SauceClient


class BaseTest(TestCase):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def setUp(self):
        env_data = EnvData()
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.test_env = env_data.get_test_env()
        self.logger.info(self.test_env)
        self.test_target = env_data.get_test_target()
        self.test_target_context = env_data.get_test_target_context()
        self.desired_capabilities = json.loads(browser_config)["target_capabilities"][
            self.test_target
        ]
        self.logger.info(self.desired_capabilities)
        # if Utils.is_sauce_enabled():
        #     desired_caps = {}
        #     self.sauce_user_name = Utils.get_sauce_user_name()
        #     self.sauce_key = Utils.get_sauce_key()
        #     desired_caps["name"] = self._testMethodName
        #     desired_caps["tunnelIdentifier"] = Utils.get_tunnel_identifier()
        #     command = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub" % (
        #         self.sauce_user_name,
        #         self.sauce_key,
        #     )
        #     self.driver = webdriver.Remote(
        #         command_executor=command, desired_capabilities=desired_caps
        #     )
        #     self.logger.info(
        #         "sesson_id=%s job_name=%s"
        #         % (str(self.driver.session_id), self._testMethodName)
        #     )
        #     sys.stdout.flush()
        if self.test_target == "desktop_chrome":
            self.logger.info("Desktop Test Target")
            self.driver = webdriver.Chrome(executable_path="/Users/Sapthagiri/Workspace/appium-mobile-testing/src/drivers/chromedriver")
        elif self.test_target == "desktop_chrome_headless":
            self.driver = webdriver.Chrome(options=chrome_options)
        else:
            self.logger.info("Mobile Test Target")

        config.DRIVER = self.driver
        config.TEST_TARGET = self.test_target
        config.TEST_TARGET_CONTEXT = self.test_target_context

    def tearDown(self):
        self.save_screen_shot(self.id())
        self.driver.quit()

    def save_screen_shot(self, name):
        dir = os.getcwd() + "/screenshots/"
        if not os.path.exists(dir):
            os.makedirs(dir)
        file_name = dir + name + ".png"
        self.logger.info(file_name)
        self.driver.save_screenshot(filename=file_name)
