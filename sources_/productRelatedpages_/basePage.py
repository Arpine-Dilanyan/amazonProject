from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        """
        Find multiple web elements based on a locator dictionary.

        Args:
            locator (dict): A dictionary containing the locator information.
                Example: {'by': By.XPATH, 'value': '//div[@class="element-class"]'}

        Returns:
            list: A list of Selenium web elements matching the provided locator.
        """
        try:
            elements = self.driver.find_elements(locator['by'], locator['value'])
            return elements
        except Exception as e:
            print(f"Elements not found: {e}")
            return []

