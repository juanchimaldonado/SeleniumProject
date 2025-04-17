from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username, password):
        self.type_text(self.EMAIL_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.wait_for_element(self.ERROR_MESSAGE).text


