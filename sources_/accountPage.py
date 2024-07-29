from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class AccountPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.yourProfilesButtonLocator = (By.XPATH, "(//div[@class='ya-card-cell']/a)[7])")

    def click_your_profiles_button(self):
        yourProfilesButtonElement = self._find_element(self.yourProfilesButtonLocator)
        yourProfilesButtonElement.click()
