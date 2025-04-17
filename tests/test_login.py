import pytest

from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_valid(driver, base_url):
    """
    Test case for valid login.
    :param driver: The WebDriver instance.
    :param base_url: The base URL of the application.
    """
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    print(driver.current_url)
    assert driver.current_url == f"{base_url}inventory.html"


def test_login_invalid(driver, base_url):
    """
    Test case for invalid login.
    :param driver: The WebDriver instance.
    :param base_url: The base URL of the application.
    """
    driver.get(base_url)
    login_page = LoginPage(driver)
    login_page.login("invalid_user", "invalid_password")
    error_message = login_page.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service"