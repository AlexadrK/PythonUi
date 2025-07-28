import allure
import pytest
import random
import time
from base.base_test import BaseTest

@allure.feature("Profile functionality")
class TestsProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Crical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.profile_page.is_opened()
        self.profile_page.change_name(f"Test{random.randint(1, 10)}")
        self.profile_page.save_changes()
        self.profile_page.is_changes_saved()
        time.sleep(2)
        self.profile_page.make_screenshot("Success")
