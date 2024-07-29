from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self.addToCartButtonLocator = (By.ID, "add-to-cart-button")

    def press_add_to_cart_button(self):
        addToCartButtonElement = self._find_element(self.addToCartButtonLocator)
        addToCartButtonElement.click()
