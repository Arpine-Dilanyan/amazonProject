from selenium import webdriver
from selenium.webdriver.common.by import By
from sources_.basePage_ import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super().__init__(driver)
        self._loginFieldsLocator = (By.ID, "ap_email")
        self._continueButtonLocator = (By.ID, "continue")
        self._passwordFieldLocator = (By.ID, "ap_password")
        self._signInButtonLocator = (By.ID, "signInSubmit")
        self._invalidPasswordMessageLocator = (By.ID, "auth-error-message-box")

    def fill_login_filed(self, login):
        """Finds the login field element using the stored locator and
        inputs the provided login text after clearing any existing text."""

        loginFiledElement = self._find_element(self._loginFieldsLocator)
        loginFiledElement.clear()
        loginFiledElement.send_keys(login)

    def press_continue_button(self):
        """ Finds the continue button element using the stored locator and clicks it.
        """
        continueButtonElement = self._find_element(self._continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password):
        """Finds the password field element using the stored
        locator and inputs the provided password text after
         clearing any existing text."""

        passwordFieldElement = self._find_element(self._passwordFieldLocator)
        passwordFieldElement.clear()
        passwordFieldElement.send_keys(password)

    def press_signin_button(self):
        """ Finds the sign-in button element using
        the stored locator and clicks it."""

        signInButtonElement = self._find_element(self._signInButtonLocator)
        signInButtonElement.click()

    def check_invalid_password_message(self):
        return self._is_element_visible(self._invalidPasswordMessageLocator)
