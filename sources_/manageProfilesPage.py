from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class ManageProfilesPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.selectProfileLocator = (By.ID, "profile-pick-actor-button-0")
        self.editProfileNameLocator = (By.ID, "name-edit-modal-link")
        self.editNameFiledLocator = (By.ID, "profile-name-text-input")
        self.saveChangesButtonLocator = (By.ID, "profile-name-edit-submit-button")

    def select_profile(self):
        selectProfileElement = self._find_element(self.selectProfileLocator)
        selectProfileElement.click()

    def click_edit_profile_name_button(self):
        editProfileNameElement = self._find_element(self.editProfileNameLocator)
        editProfileNameElement.click()

    def edit_name_filed(self, text):
        editNameFiledElement = self._find_element(self.editNameFiledLocator)
        editNameFiledElement.clear()
        editNameFiledElement.send_keys(text)

    def press_save_changes_button(self):
        saveChangesButtonElement = self._find_element(self.saveChangesButtonLocator)
        saveChangesButtonElement.click()
