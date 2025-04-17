from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):

    ITEMS_LIST = (By.XPATH, "//div[@class='cart_list']/div[@class='cart_item']")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_items(self):
        """
        Returns a list of items in the cart.
        :return: List of items in the cart.
        """
        items = self.wait_for_elements(self.ITEMS_LIST)
        item_names = []
        for item in items:
            name = item.find_element(*self.ITEM_NAME).text
            item_names.append(name)
        return item_names