import time

import allure
from selenium.webdriver import Keys

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):

    PAGE_URL = Links.PROFILE_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit'][1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    #@allure.step("Change name")
    def change_name(self, new_name):
        with allure.step(f"Change name on {new_name}"):
            firs_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            firs_name_field.click()
            firs_name_field.send_keys(Keys.CONTROL + "A")
            firs_name_field.send_keys(Keys.BACKSPACE)
            #firs_name_field.clear()
            # assert firs_name_field.get_attribute("value") =="", "There is some text"
            firs_name_field.send_keys(new_name)
            #time.sleep(5)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Changes successfully saved")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))