import pytest
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.regression
def test_item_added_to_cart(driver, base_url):
    """
    Test case for adding an item to the cart.
    :param driver: The WebDriver instance.
    :param base_url: The base URL of the application.
    """
    driver.get(base_url)

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)

    # Add item to cart
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory_page.click_cart_button()

    # Verify item is in cart
    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()

    assert "Sauce Labs Backpack" in cart_items, "Item not found in cart"