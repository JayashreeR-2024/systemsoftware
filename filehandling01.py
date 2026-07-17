import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# File paths
valid_file = str(Path("test_files/valid_file.pdf").absolute())
invalid_file = str(Path("test_files/invalid_file.exe").absolute())


driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:

    # Open local HTML page
    driver.get(
        "file:///C:/Users/Jayashree%20R/PycharmProjects/pythonProject/systemsoftware/upload.html"
    )


    # -----------------------------
    # Test valid file upload
    # -----------------------------

    upload = wait.until(
        EC.presence_of_element_located(
            (By.ID, "fileUpload")
        )
    )

    upload.send_keys(valid_file)

    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()


    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    assert message.text == "Upload Successful"

    print("✅ Valid file upload passed")


    # -----------------------------
    # Test invalid file upload
    # -----------------------------

    driver.refresh()

    upload = wait.until(
        EC.presence_of_element_located(
            (By.ID, "fileUpload")
        )
    )

    upload.send_keys(invalid_file)

    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()


    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )

    assert message.text == "Unsupported file format"

    print("✅ Invalid file rejection passed")


finally:
    time.sleep(2)
    driver.quit()