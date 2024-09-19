import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPurchase:
    def setup_method(self) -> None:
        self.chrome_path = ChromeDriverManager().install()
        self.options = ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--incognito')
        self.browser_service = Service(executable_path=self.chrome_path)
        self.browser = Chrome(service=self.browser_service, options=self.options)

    @pytest.mark.parametrize(
        'product, expected',
        (
                ['Sauce Labs Backpack', 'Checkout: Complete!'],
        )
    )
    def test_purchase(self, product: str, expected: str) -> None:
        self.browser.get('https://www.saucedemo.com')
        username_field = self.browser.find_element(by=By.ID, value='user-name')
        username_field.send_keys('standard_user')
        password_field = self.browser.find_element(by=By.ID, value='password')
        password_field.send_keys('secret_sauce')
        submit_button = self.browser.find_element(by=By.ID, value='login-button')
        submit_button.click()
        add_to_cart_button = self.browser.find_element(by=By.ID, value='add-to-cart-sauce-labs-backpack')
        add_to_cart_button.click()
        cart_button = self.browser.find_element(by=By.CLASS_NAME, value='shopping_cart_link')
        cart_button.click()
        product_name = self.browser.find_element(by=By.CLASS_NAME, value='inventory_item_name')
        assert product_name.text == product
        checkout_button = self.browser.find_element(by=By.ID, value='checkout')
        checkout_button.click()
        first_name_field = self.browser.find_element(by=By.ID, value='first-name')
        first_name_field.send_keys('first-name')
        last_name_field = self.browser.find_element(by=By.ID, value='last-name')
        last_name_field.send_keys('last-name')
        postal_code_field = self.browser.find_element(by=By.ID, value='postal-code')
        postal_code_field.send_keys('postal-code')
        continue_button = self.browser.find_element(by=By.ID, value='continue')
        continue_button.click()
        finish_button = self.browser.find_element(by=By.ID, value='finish')
        finish_button.click()
        result = self.browser.find_element(by=By.CLASS_NAME, value='title')
        assert result.text == expected
