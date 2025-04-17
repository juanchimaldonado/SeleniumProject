from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import element_to_be_selected
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """
        Navigate to a specified URL.
        :param url: The URL to navigate to.
        """
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        """
        Wait for an element to be present in the DOM and visible on the page.
        :param locator: The locator of the element to wait for.
        :param timeout: The maximum time to wait for the element (in seconds).
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_elements(self, locator, timeout=10):
        """
        Wait for elements to be present in the DOM and visible on the page.
        :param locator: The locator of the elements to wait for.
        :param timeout: The maximum time to wait for the elements (in seconds).
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def click_element(self, locator):
        """
        Click on an element.
        :param locator: The locator of the element to click.
        """
        element = self.wait_for_element(locator)
        element.click()

    def type_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def select_from_dropdown_by_text(self, locator, text):
        """
        Select an option from a dropdown by visible text.
        :param locator: The locator of the dropdown element.
        :param text: The visible text of the option to select.
        """
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_visible_text(text)

    def select_from_dropdown_by_index(self, locator, value):
        """
        Select an option from a dropdown by index.
        :param locator: The locator of the dropdown element.
        :param value: The value of the index.
        """
        dropdown = Select(self.wait_for_element(locator))
        dropdown.select_by_index(value)

    def get_select_options(self, locator):
        """
        Get all options from a dropdown.
        :param locator: The locator of the dropdown element.
        :return: A list of option texts.
        """
        dropdown = Select(self.wait_for_element(locator))
        return [option.text for option in dropdown.options]

    def select_element(self, locator):
        """
        Select an Element.
        :param locator: The locator of the element.
        """
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()

    def deselect_checkbox(self, locator):
        """
        Deselect a checkbox.
        :param locator: The locator of the checkbox element.
        """
        checkbox = self.wait_for_element(locator)
        if checkbox.is_selected():
            checkbox.click()

    def hover_over_element(self, locator):
        """
        Hover over an element.
        :param locator: The locator of the element to hover over.
        """
        element = self.wait_for_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()