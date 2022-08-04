# 4. Verify user able to edit any object

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://login.salesforce.com")

expected_title = "Login | Salesforce"
actual_title = driver.title

if expected_title == actual_title:
    assert True
    main_page1 = driver.current_window_handle
    driver.find_element(By.ID, "username").send_keys("OrgRup@360dc.com")
    driver.find_element(By.ID, "password").send_keys("Rupali@1996")
    driver.find_element(By.ID, "Login").click()

    time.sleep(6)
    driver.find_element(By.ID, "tryLexDialogX").click()

    time.sleep(7)
    driver.find_element(By.CLASS_NAME, "brandPrimaryFgr").click()

    time.sleep(8)
    # driver.find_element(By.XPATH, '//input[contains(@class="btn") and contains(@name,"go")]').click()

    b = driver.find_element(By.XPATH, '//input[starts-with(@class,"btn")]')
    driver.execute_script("arguments[0].click();", b)

    time.sleep(7)
    # driver.find_element(By.XPATH, '//a[contains(text,"Edit")]').click()

    # time.sleep(8)
    driver.quit()
