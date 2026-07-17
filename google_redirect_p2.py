from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")

# Launch Chrome
driver = webdriver.Chrome(options=options)

try:
    # Redirect/Open Google
    driver.get("https://www.google.com")

    # Verify page title contains Google
    assert "Google" in driver.title

    print("Test Passed: Successfully redirected to Google")
    print("Title:", driver.title)

    time.sleep(3)

finally:
    driver.quit()