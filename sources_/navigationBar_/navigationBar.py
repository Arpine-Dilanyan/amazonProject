from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class NavigationBar(BasePage):

    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.searchFiledLocator = (By.ID, "twotabsearchtextbox")
        self.findButtonLocator = (By.ID, "nav-search-submit-button")
        self.cartCountLocator = (By.ID, "nav-cart-count")
        self.loggedUserDataLocator = (By.ID, "nav-al-profile")
        self.accountModalListLocator = (By.CLASS_NAME, "nav-line-1-container")
        self.accountModalListsLocator = (By.CLASS_NAME, "nav-line-1-container")

    def click_to_account_modal_lists(self):
        accountModalLists = self._find_element(self.accountModalListLocator)
        accountModalLists.click()

    def hover_account_modal_lists(self):
        accountModalLists = self._find_element(self.accountModalListLocator)
        self._mouse_move(accountModalLists)

    def fill_search_field(self, text="AGV Helmet"):
        searchFieldElement = self._find_element(self.searchFiledLocator)
        searchFieldElement.clear()
        searchFieldElement.send_keys(text)

    def press_find_button(self):
        findButtonElement = self._find_element(self.findButtonLocator)
        self._click_to_element(findButtonElement)

    def get_cart_count(self):
        cartCountElement = self._find_element(self.cartCountLocator)
        return int(cartCountElement.text)

    def check_logged_user_data(self):
        return self._is_element_visible(self.loggedUserDataLocator)

    def go_to_profile_settings(self):
        pass
