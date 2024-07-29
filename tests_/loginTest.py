import unittest
from selenium.webdriver.support.events import EventFiringWebDriver
from common_.utilitis_.customListner import MyListener
from selenium import webdriver
from sources_.login_.loginPage import LoginPage
from common.htmlRunner_ import data_
from sources_.navigationBar_.navigationBar import NavigationBar
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.simpleDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(12)
        self.driver.maximize_window()
        self.driver.get(data_.urlSignIn)
        self.loginPageObj = LoginPage(self.driver)

    def test_positive_login(self):
        self.loginPageObj.fill_login_filed(data_.loginDataValidArpine["username"])
        self.loginPageObj.press_continue_button()
        self.loginPageObj.fill_password_field(data_.loginDataValidArpine["password"])
        self.loginPageObj.press_signin_button()

        self.navigationBarPageObj = NavigationBar(self.driver)
        self.navigationBarPageObj.hover_account_modal_lists()

        """ Assert that the login is successful """
        assert self.navigationBarPageObj.check_logged_user_data(), "ERROR Message "

    def test_negative_login(self):
        self.loginPageObj.fill_login_filed(data_.loginDataValidArpine["username"])
        self.loginPageObj.press_continue_button()
        self.loginPageObj.fill_password_field(data_.loginDataWithInvalidPasswordArpine["password"])
        self.loginPageObj.press_signin_button()

        """ If the password when you enter an invalid password"""
        assert self.loginPageObj.check_invalid_password_message(), "TRY AGAIN"

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
