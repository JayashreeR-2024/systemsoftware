from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("file:///C:/Users/Jayashree R/PycharmProjects/pythonProject/systemsoftware/students.html")

# Page 1
rows = driver.find_elements(By.XPATH, "//tbody/tr")

page1 = [r.text for r in rows]

print("Page 1:", page1)

assert len(page1) == 10

# Click Next
driver.find_element(By.XPATH, "//button[text()='Next']").click()

time.sleep(1)

# Page 2
rows = driver.find_elements(By.XPATH, "//tbody/tr")

page2 = [r.text for r in rows]

print("Page 2:", page2)

assert len(page2) == 10

assert page1 != page2

page = driver.find_element(By.ID, "pageNo").text

assert page == "2"

total = driver.find_element(By.ID, "totalRecords").text

assert total == "20"

print("Pagination Test Passed")

driver.quit()