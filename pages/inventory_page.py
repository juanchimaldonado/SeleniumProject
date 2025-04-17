from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):

    #Locators
    CART_BUTTON = (By.XPATH, "//a[@class='shopping_cart_link']")
    PRODUCTS_LIST = (By.XPATH, "//div[@class='inventory_item']")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name ")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    #Methods
    def add_item_to_cart_by_name(self, item_name):
        """
        Clicks the 'Add to cart' button for a specific item by its name.
        :param item_name: The exact name of the item (as shown in UI).
        """
        items = self.wait_for_elements(self.PRODUCTS_LIST)

        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text
            if name == item_name:
                item.find_element(*self.ADD_TO_CART_BUTTON).click()
                return True
        raise Exception(f"Item with name '{item_name}' not found.")

    def click_cart_button(self):
        """
        Clicks the cart button to navigate to the cart page.
        """
        self.click_element(self.CART_BUTTON)