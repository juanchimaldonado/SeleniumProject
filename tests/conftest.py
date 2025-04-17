import pytest
import configparser
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def pytest_addoption(parser):
    """
    Add command line options for pytest.
    :param parser: The pytest parser object.
    """
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser: chrome, firefox, edge, safari")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def driver(browser):
    """
    Fixture to set up and tear down the WebDriver.
    :return: WebDriver instance.
    """
    if browser == "chrome":
        options = ChromeOptions()
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    elif browser == "edge":
        options = EdgeOptions()
        service = EdgeService(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Browser '{browser}' is not supported.")

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    config = configparser.ConfigParser()
    config_path = Path(__file__).resolve().parent.parent / 'config.ini'
    config.read(config_path)
    return config['qa']['base_url']