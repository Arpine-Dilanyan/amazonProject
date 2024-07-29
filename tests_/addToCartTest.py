import unittest
from selenium import webdriver
from sources_.login_.loginPage import LoginPage
from sources_.navigationBar_.navigationBar import NavigationBar
from sources_.productRelatedpages_.productDetailsPage import ProductDetailsPage
from sources_.productRelatedpages_.searchResultPage import SearchResultPage
from common.htmlRunner_ import data_


class AddToCartTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(data_.urlSignIn)
        self.loginPageObj = LoginPage(self.driver)
        self.navigationBarPageObj = NavigationBar(self.driver)
        self.searchResultPageObj = SearchResultPage(self.driver)
        self.productDetailsPageObj = ProductDetailsPage(self.driver)

    def test_add_to_cart_with_logged_user(self):
        self.loginPageObj.fill_login_filed(data_.loginDataValidArpine["username"])
        self.loginPageObj.press_continue_button()
        self.loginPageObj.fill_password_field(data_.loginDataValidArpine["password"])
        self.loginPageObj.press_signin_button()

        self.navigationBarPageObj.fill_search_field("AGV GP PISTA")
        self.navigationBarPageObj.press_find_button()
        self.searchResultPageObj.press_first_product_from_result()

        cartCount = self.navigationBarPageObj.get_cart_count()
        self.productDetailsPageObj.press_add_to_cart_button()
        cartCount1 = self.navigationBarPageObj.get_cart_count()

        """If the assertion passes, you can be confident that 
        the "add to cart" action succeeded, and the 
        product was added to the cart.
        """
        assert cartCount1 == cartCount + 1, f"Expected cart count: {cartCount + 1}, Actual cart count: {cartCount1}"

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
