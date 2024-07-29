from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from common_.utilitis_.coustomLogger import *  # Assuming this imports necessary logging functions


class BasePage:
    def __init__(self, driver: webdriver.Chrome):
        """
        Initialize the BasePage with a WebDriver instance.

        :param driver: WebDriver instance (e.g., Chrome WebDriver)
        """
        self.driver = driver

    def _find_element(self, locator):
        """
        Find an element if it is visible.

        :param locator: Locator tuple for the element (e.g., (By.ID, 'element_id'))
        :return: WebElement if found and visible
        """
        if self._is_element_visible(locator):
            element = self.driver.find_element(*locator)
            return element
        else:
            print("ERROR: Element not found")
            exit(1)

    def _is_element_visible(self, locator):
        """
        Check if an element is visible on the page.

        :param locator: Locator tuple for the element
        :return: True if the element is visible, False otherwise
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def _element_should_be_visible(self, locator):
        """
        Wait for an element to be visible. Print an error message if it is not.

        :param locator: Locator tuple for the element
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except:
            print("ERROR: Element not visible but should be")

    def _get_title(self):
        """
        Get the title of the current page.

        :return: Title of the current page
        """
        return self.driver.title

    def _fill_field(self, element, text):
        """
        Clear a field and enter text.

        :param element: WebElement of the field
        :param text: Text to enter into the field
        """
        element.clear()
        element.send_keys(text)

    def _mouse_move(self, element):
        """
        Move the mouse to the specified element.

        :param element: WebElement to move the mouse to
        """
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def _click_to_element(self, element):
        """
        Click on an element after ensuring it is clickable.

        :param element: WebElement to click
        """
        try:
            WebDriverWait(self.driver, 10).until(self.is_element_clickable(element))
            element.click()
            print("Element clicked")
        except:
            print("Timeout waiting for the element to be clickable")
            exit(2)

    def is_element_clickable(self, element):
        """
        Check if an element is clickable.

        :param element: WebElement to check
        :return: Function that checks if the element is enabled and displayed
        """
        print("Element is clickable")
        return lambda driver: element.is_enabled() and element.is_displayed()

    def _drag_and_drop(self):
        """
        Placeholder for drag and drop functionality.
        """
        pass

    def _press_and_hold(self):
        """
        Placeholder for press and hold functionality.
        """
        pass

    def _get_element_text(self, webElement):
        """
        Get the text of an element.

        :param webElement: WebElement to get text from
        :return: Text of the element
        """
        return webElement.text

    def _get_element_text_by_locator(self, locator):
        """
        Get the text of an element found by a locator.

        :param locator: Locator tuple for the element
        :return: Text of the found element
        """
        element = self._find_element(locator)
        return element.text

    def _double_click(self):
        """
        Placeholder for double-click functionality.
        """
        pass
