import time
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----------------------------
# File locations
# -----------------------------

valid_file = str(Path("test_files/valid_file.pdf").absolute())
invalid_file = str(Path("test_files/invalid_file.exe").absolute())

HTML_PATH = (
    "file:///C:/Users/Jayashree%20R/"
    "PycharmProjects/pythonProject/systemsoftware/upload.html"
)


# Verify files exist
print("Valid file:", valid_file)
print("Exists:", os.path.exists(valid_file))

print("Invalid file:", invalid_file)
print("Exists:", os.path.exists(invalid_file))


# -----------------------------
# Start browser
# -----------------------------

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 10)


try:

    # Open upload page
    driver.get(HTML_PATH)

    time.sleep(3)

    # =====================================
    # Test 1: Valid file upload
    # =====================================

    print("Testing valid file upload...")

    upload_box = wait.until(
        EC.presence_of_element_located(
            (By.ID, "fileUpload")
        )
    )

    upload_box.send_keys(valid_file)

    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()


    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )


    if message.text == "Upload Successful":
        print("✅ Valid file upload passed")
    else:
        print("❌ Valid upload failed:", message.text)



    # =====================================
    # Test 2: Invalid file upload
    # =====================================

    print("Testing invalid file upload...")

    driver.refresh()

    time.sleep(2)

    upload_box = wait.until(
        EC.presence_of_element_located(
            (By.ID, "fileUpload")
        )
    )

    upload_box.send_keys(invalid_file)

    driver.find_element(
        By.TAG_NAME,
        "button"
    ).click()


    message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "message")
        )
    )


    if message.text == "Unsupported file format":
        print("✅ Unsupported file rejection passed")
    else:
        print("❌ Invalid file test failed:", message.text)



    # Keep browser open for checking
    input("\nPress Enter to close browser...")


finally:

    driver.quit()