from selenium import webdriver
from sources_.basePage_ import BasePage


class CartPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)

    def delete_product_from_cart(self):
        pass
