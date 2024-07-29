from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class AccountModalLists(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.accountButtonFromModalLocator = (By.LINK_TEXT, "Account")

    def click_to_account_button_from_modal(self):
        accountButtonFromModalElement = self._find_element(self.accountButtonFromModalLocator)
        accountButtonFromModalElement.click()

