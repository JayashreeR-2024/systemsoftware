from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

file = open("demo_student_validation.csv", "r")

try:
    driver.get("https://your-app.com/login")

    # ---------------- LOGIN ----------------
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("admin")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("admin123")
    wait.until(EC.element_to_be_clickable((By.ID, "loginBtn"))).click()

    # ---------------- READ CSV LINE BY LINE ----------------
    lines = file.readlines()

    # Skip header
    for i in range(1, len(lines)):
        data = lines[i].strip().split(",")

        test_id = data[0]
        scenario = data[1]
        usn = data[2]
        name = data[3]
        expected = data[4]

        print("Running:", test_id, scenario)

        # Navigate to student module
        wait.until(EC.element_to_be_clickable((By.ID, "studentMenu"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "addStudentBtn"))).click()

        # Fill form
        wait.until(EC.presence_of_element_located((By.ID, "usn"))).clear()
        driver.find_element(By.ID, "usn").send_keys(usn)

        driver.find_element(By.ID, "name").clear()
        driver.find_element(By.ID, "name").send_keys(name)

        driver.find_element(By.ID, "submitBtn").click()

        # Check result
        try:
            msg = wait.until(
                EC.visibility_of_element_located((By.ID, "errorMessage"))
            ).text.lower()

            print("Validation message:", msg)

        except:
            print("No error message (record may be accepted)")

    print("CSV test execution completed")

except Exception as e:
    print("Test FAILED:", str(e))

finally:
    file.close()
    driver.quit()