from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # login
    wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
    wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    time.sleep(3)
    print("Logged in:", driver.current_url)

    # simulate inactivity
    time.sleep(60)

    # try accessing dashboard
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    time.sleep(3)

    print("After timeout URL:", driver.current_url)

except Exception as e:
    print("Error:", str(e))

finally:
    driver.quit()