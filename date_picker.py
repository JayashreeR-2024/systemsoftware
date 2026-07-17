from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

date_box = driver.find_element(By.ID, "datepicker")

yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y%m%d")

print("Yesterday:", yesterday)
print("Tomorrow:", tomorrow)

# -------------------------
# TC1: Past Date Check
# -------------------------
date_box.clear()
date_box.send_keys(yesterday)

past_value = date_box.get_attribute("value").replace("-", "")
print("Selected Past Date:", past_value)

if past_value == yesterday:
    print("✔ Past date is allowed (No validation in application)")
else:
    print("✔ Past date is blocked")

# -------------------------
# TC2: Future Date Check
# -------------------------
date_box.clear()
date_box.send_keys(tomorrow)

future_value = date_box.get_attribute("value").replace("-", "")
print("Selected Future Date:", future_value)

if future_value == tomorrow:
    print("✔ Future date accepted")
else:
    print("✘ Future date not accepted")

print("Date Picker Test Completed")

driver.quit()