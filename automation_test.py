from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time


fake = Faker()

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 30)


try:

    # -----------------------------
    # Invalid Login Test
    # -----------------------------

    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys("wrong_user")


    driver.find_element(
        By.ID,
        "password"
    ).send_keys("wrong_password")


    driver.find_element(
        By.ID,
        "login-button"
    ).click()


    error = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "h3[data-test='error']")
        )
    )


    assert "Username and password do not match" in error.text

    print("✅ Invalid login validation passed")



    # -----------------------------
    # Valid Login
    # -----------------------------

    driver.get("https://www.saucedemo.com/")

    driver.find_element(
        By.ID,
        "user-name"
    ).send_keys("standard_user")


    driver.find_element(
        By.ID,
        "password"
    ).send_keys("secret_sauce")


    driver.find_element(
        By.ID,
        "login-button"
    ).click()



    wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_list")
        )
    )


    print("✅ Login successful")



    # -----------------------------
    # Product Filtering
    # -----------------------------

    driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    ).send_keys("Price (low to high)")


    print("✅ Product sorting completed")



    # -----------------------------
    # Add Multiple Products
    # -----------------------------

    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    ).click()


    driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-bike-light"
    ).click()



    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()



    cart_items = driver.find_elements(
        By.CLASS_NAME,
        "cart_item"
    )


    assert len(cart_items) == 2


    print("✅ Multiple products added to cart")



    # -----------------------------
    # Quantity Verification
    # -----------------------------

    quantity = driver.find_element(
        By.CLASS_NAME,
        "cart_quantity"
    ).text


    assert quantity == "1"


    print("✅ Product quantity verified")



finally:

    time.sleep(3)
    driver.quit()