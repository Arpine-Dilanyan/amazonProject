from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class SearchResultPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.firstProductLocator = (By.XPATH, "(//a[@class='a-link-normal s-no-outline'])[1]")

    def press_first_product_from_result(self):
        firstProductElement = self._find_element(self.firstProductLocator)
        firstProductElement.click()
