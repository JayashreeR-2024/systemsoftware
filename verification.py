from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")

# ---------------------------------------------------
# TEST CASES (for reference inside automation script)
# ---------------------------------------------------

# TC1: Verify table loads successfully
# Expected: Table should be visible on page load

# TC2: Verify ascending sort on Last Name column
# Expected: Data should be sorted A → Z

# TC3: Verify descending sort on Last Name column
# Expected: Data should be sorted Z → A

# TC4: Verify record count remains same after sorting
# Expected: No data loss after sorting

# ---------------------------------------------------

# Function to get Last Name column values
def get_last_names():
    rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
    return [row.find_element(By.XPATH, "./td[1]").text for row in rows]

# Step 1: Capture initial data
before_sort = get_last_names()
print("Before Sort:", before_sort)

# Step 2: Click header for ascending sort
header = driver.find_element(By.XPATH, "//table[@id='table1']//span[text()='Last Name']")
header.click()

asc_data = get_last_names()
print("Ascending:", asc_data)

assert asc_data == sorted(asc_data), "Ascending sort failed (TC2 Failed)"

# Step 3: Click header for descending sort
header.click()

desc_data = get_last_names()
print("Descending:", desc_data)

assert desc_data == sorted(desc_data, reverse=True), "Descending sort failed (TC3 Failed)"

# Step 4: Validate record count remains same
assert len(before_sort) == len(asc_data) == len(desc_data), "Record count mismatch (TC4 Failed)"

print("All Sorting Test Cases Passed Successfully!")

driver.quit()