import time
import openpyxl

from faker import Faker

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


fake = Faker()


# ==================================================
# 1. CREATE EXCEL TEST DATA USING FAKER
# ==================================================

excel_file = "testdata.xlsx"


def create_excel_data():

    workbook = openpyxl.Workbook()

    sheet = workbook.active
    sheet.title = "Login"

    sheet.append(
        [
            "username",
            "password",
            "email",
            "first_name",
            "last_name"
        ]
    )


    for i in range(10):

        sheet.append(
            [
                fake.user_name(),
                fake.password(length=10),
                fake.email(),
                fake.first_name(),
                fake.last_name()
            ]
        )


    workbook.save(excel_file)

    print("Excel file created successfully")



# ==================================================
# 2. READ EXCEL DATA
# ==================================================

def read_excel_data():

    workbook = openpyxl.load_workbook(
        excel_file
    )

    sheet = workbook["Login"]


    username = sheet["A2"].value
    password = sheet["B2"].value
    email = sheet["C2"].value
    firstname = sheet["D2"].value
    lastname = sheet["E2"].value


    return (
        username,
        password,
        email,
        firstname,
        lastname
    )



# Create Excel
create_excel_data()


(
username,
password,
email,
firstname,
lastname

) = read_excel_data()



# ==================================================
# 3. START SELENIUM
# ==================================================

driver = webdriver.Chrome()

driver.maximize_window()

wait = WebDriverWait(
    driver,
    15
)



# ==================================================
# 4. CONTACT FORM TEST
# ==================================================

def contact_form_test():

    driver.get(
        "https://yourwebsite.com/contact"
    )


    driver.find_element(
        By.ID,
        "name"
    ).send_keys(
        fake.name()
    )


    driver.find_element(
        By.ID,
        "email"
    ).send_keys(
        fake.email()
    )


    driver.find_element(
        By.ID,
        "message"
    ).send_keys(
        fake.text()
    )


    driver.find_element(
        By.ID,
        "submit"
    ).click()


    message = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "successMessage"
            )
        )
    )


    assert "Thank" in message.text

    print(
        "PASS: Contact form submitted"
    )



# ==================================================
# 5. INVALID LOGIN TEST
# ==================================================

def invalid_login_test():

    driver.get(
        "https://yourwebsite.com/login"
    )


    driver.find_element(
        By.ID,
        "username"
    ).send_keys(
        username
    )


    driver.find_element(
        By.ID,
        "password"
    ).send_keys(
        password
    )


    driver.find_element(
        By.ID,
        "loginButton"
    ).click()



    error = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "errorMessage"
            )
        )
    )


    assert "Invalid" in error.text


    print(
        "PASS: Invalid login error displayed"
    )



# ==================================================
# 6. USER REGISTRATION TEST
# ==================================================

def registration_test():

    driver.get(
        "https://yourwebsite.com/register"
    )


    driver.find_element(
        By.ID,
        "firstName"
    ).send_keys(
        firstname
    )


    driver.find_element(
        By.ID,
        "lastName"
    ).send_keys(
        lastname
    )


    driver.find_element(
        By.ID,
        "email"
    ).send_keys(
        email
    )


    new_password = fake.password()


    driver.find_element(
        By.ID,
        "password"
    ).send_keys(
        new_password
    )


    driver.find_element(
        By.ID,
        "confirmPassword"
    ).send_keys(
        new_password
    )


    driver.find_element(
        By.ID,
        "register"
    ).click()


    success = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "successMessage"
            )
        )
    )


    print(
        "PASS: Registration completed"
    )



# ==================================================
# 7. EMAIL VALIDATION TEST
# ==================================================

def email_validation_test():

    driver.get(
        "https://yourwebsite.com/register"
    )


    driver.find_element(
        By.ID,
        "email"
    ).send_keys(
        "invalidemail"
    )


    driver.find_element(
        By.ID,
        "register"
    ).click()



    error = wait.until(
        EC.visibility_of_element_located(
            (
                By.ID,
                "emailError"
            )
        )
    )


    assert "valid" in error.text.lower()


    print(
        "PASS: Email validation"
    )



# ==================================================
# 8. PRODUCT FILTER TEST
# ==================================================

def product_filter_test():

    driver.get(
        "https://yourwebsite.com/products"
    )


    driver.find_element(
        By.ID,
        "category"
    ).send_keys(
        "Electronics"
    )


    driver.find_element(
        By.ID,
        "minPrice"
    ).send_keys(
        "100"
    )


    driver.find_element(
        By.ID,
        "maxPrice"
    ).send_keys(
        "500"
    )


    driver.find_element(
        By.ID,
        "filter"
    ).click()



    products = driver.find_elements(
        By.CLASS_NAME,
        "product"
    )


    assert len(products) > 0


    print(
        "PASS: Product filtering"
    )



# ==================================================
# 9. CART TEST
# ==================================================

def cart_test():

    driver.get(
        "https://yourwebsite.com/products"
    )


    driver.find_element(
        By.ID,
        "addProduct1"
    ).click()


    driver.find_element(
        By.ID,
        "addProduct2"
    ).click()



    driver.find_element(
        By.ID,
        "cart"
    ).click()



    items = driver.find_elements(
        By.CLASS_NAME,
        "cartItem"
    )


    assert len(items) == 2


    print(
        "PASS: Multiple products added"
    )



    # Quantity update

    quantity = driver.find_element(
        By.ID,
        "quantity"
    )

    quantity.clear()

    quantity.send_keys(
        "3"
    )


    driver.find_element(
        By.ID,
        "updateCart"
    ).click()



    updated_quantity = driver.find_element(
        By.ID,
        "quantity"
    ).get_attribute(
        "value"
    )


    assert updated_quantity == "3"


    print(
        "PASS: Quantity updated"
    )



    # Cart total

    total = driver.find_element(
        By.ID,
        "cartTotal"
    ).text


    print(
        "Cart Total:",
        total
    )



# ==================================================
# RUN ALL TESTS
# ==================================================

try:

    contact_form_test()

    invalid_login_test()

    registration_test()

    email_validation_test()

    product_filter_test()

    cart_test()


finally:

    time.sleep(3)

    driver.quit()