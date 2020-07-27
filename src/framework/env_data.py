import json
import os
from src.framework.env_config import config_data
import logging


class EnvData(object):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    environment = json.loads(config_data)

    test_env = (
        os.environ.get("TEST_ENV") if os.environ.get("TEST_ENV") is not None else "STG"
    )

    test_target = (
        os.environ.get("TEST_TARGET")
        if os.environ.get("TEST_TARGET") is not None
        else "desktop_chrome"
    )

    def get_test_env(self):
        return self.test_env

    def get_test_target(self):
        return self.test_target

    def get_test_target_context(self):
        return self.test_target.split("_")[0]

    def get_api_host(self):
        if self.test_env == "STG":
            return self.environment[self.test_env]["API_HOST"]
        elif self.test_env == "DEV":
            return self.environment[self.test_env]["DEV_URL"]

    def get_app_host(self):
        self.logger.info(self.get_test_env())
        if self.test_env == "STG":
            return self.environment[self.test_env]["APP_HOST"]
        elif self.test_env == "DEV":
            return self.environment[self.test_env]["DEV_APP_URL"]

    def get_admin_url(self):
        if self.test_env == "STG":
            return self.environment[self.test_env]["ADMIN_URL"]
        elif self.test_env == "DEV":
            return self.environment[self.test_env]["DEV_ADMIN_URL"]

    def is_sauce_enabled(self):
        return self.environment[self.test_env]["SAUCE_RUN"]

    def get_sauce_user_name(self):
        return self.environment[self.test_env]["SAUCE_USER_NAME"]

    def get_sauce_key(self):
        return self.environment[self.test_env]["SAUCE_KEY"]

    def get_tunnel_identifier(self):
        return self.environment[self.test_env]["TUNNEL_IDENTIFIER"]

    def get_form_fly_url(self):
        return self.environment[self.test_env]["FORM_FLY_URL"]

    def get_test_target_context_headless(self):
        return self.test_target.split("_")[2]

    def get_sap_app_url(self):
        if self.test_env == "STG" or self.test_env == "DEV":
            return self.environment[self.test_env]["SAP_APP_URL"]

    def get_mailinator_token(self):
        self.logger.info(os.environ.get("MAILINATOR_TOKEN"))
        if os.environ.get("MAILINATOR_TOKEN") is not None:
            return os.environ.get("MAILINATOR_TOKEN")
        else:
            pass
