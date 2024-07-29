from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class ChooseYourLocationPopUp(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.popoverButtonLocator = (By.ID, "nav-global-location-popover-link")
        self.zipCodeFieldLocator = (By.CLASS_NAME, "GLUX_Full_Width a-declarative")
        self.doneButtonLocator = (By.CLASS_NAME, "a-button-text")
        self.applyButtonLocator = (By.ID, "GLUXZipUpdate")

    def click_popover_button(self):
        popoverButtonElement = self._find_element(self.popoverButtonLocator)
        popoverButtonElement.click()

    def fill_zip_code_field(self, text=98170):
        zipCodeFieldElement = self._find_element(self.zipCodeFieldLocator)
        zipCodeFieldElement.send_keys(text)

    def press_apply_button(self):
        applyButtonElement = self._find_element(self.applyButtonLocator)
        applyButtonElement.click()

    def press_done_button(self):
        doneButtonElement = self._find_element(self.doneButtonLocator)
        doneButtonElement.clcik()
