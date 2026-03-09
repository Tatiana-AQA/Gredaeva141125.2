import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import pytest
import faker

class TestFullPurchaseFlow:

    LOGIN_FIELD = ("xpath", "//input[@id='user-name']")
    PASSWORD_FIELD = ("xpath", "//input[@id='password']")
    SUBMIT_BUTTON = ("xpath", "//input[@id='login-button']")
    S_LABS_1 = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
    SHOPPING_CART = ("xpath", "//a[@class='shopping_cart_link']")
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")
    CONTINUE_BUTTON = ("xpath", "//input[@id='continue']")
    FINISH_BUTTON = ("xpath", "//button[@id='finish']")

    def test_full_purchase_flow(self, user, driver):
        options = Options()
        options.add_argument("--incognito")
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
                                        )
        driver = webdriver.Chrome(options=options)
        actions = ActionChains(driver)
        driver.get("https://www.saucedemo.com")
        driver.find_element(*self.LOGIN_FIELD).send_keys("standard_user")
        driver.find_element(*self.PASSWORD_FIELD).send_keys("secret_sauce")
        time.sleep(3)
        driver.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(3)

        assert driver.current_url == "https://www.saucedemo.com/inventory.html", "ERROR"

        element_labs_1 = driver.find_element(*self.S_LABS_1)
        element_cart = driver.find_element(*self.SHOPPING_CART)
        actions.click(element_labs_1).perform()
        time.sleep(3)
        actions.click(element_cart).perform()
        time.sleep(3)

        assert driver.current_url == "https://www.saucedemo.com/cart.html", "ERROR"

        element_checkout_button = driver.find_element(*self.CHECKOUT_BUTTON)
        actions.click(element_checkout_button).perform()
        time.sleep(3)

        assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "ERROR"

        first_name = driver.find_element("xpath", "//input[@id='first-name']")
        last_name = driver.find_element("xpath", "//input[@id='last-name']")
        postal_code = driver.find_element("xpath", "//input[@id='postal-code']")
        first_name.clear()
        first_name.send_keys(self.first_name_user)
        last_name.clear()
        last_name.send_keys(self.last_name_user)
        postal_code.clear()
        postal_code.send_keys(self.postal_code_user)
        time.sleep(3)
        CONTINUE_BUTTON = ("xpath", "//input[@id='continue']")
        element_continue_button = driver.find_element(*CONTINUE_BUTTON)
        actions.click(element_continue_button).perform()
        time.sleep(3)

        assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "ERROR"

        FINISH_BUTTON = ("xpath", "//button[@id='finish']")
        element_finish_button = driver.find_element(*FINISH_BUTTON)
        actions.click(element_finish_button).perform()
        time.sleep(3)

