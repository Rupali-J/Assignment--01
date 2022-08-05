# 4. Verify user able to edit any object

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://login.salesforce.com")
driver.maximize_window()
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
    driver.find_element(By.XPATH, "//a[@id='setupLink']").click()

    time.sleep(5)
    # CLICK ON CREATE OPTION BELOW QUICK FIND BOX
    driver.find_element(By.ID, "DevTools_font").click()
    # CLICK ON OBJECTS INSIDE CREATE
    driver.find_element(By.ID, "CustomObjects_font").click()
    # CLICK ON OBJECT NAME
    driver.find_element(By.LINK_TEXT, "Custon object1").click()
    driver.find_element(By.NAME, "edit").click()
    driver.find_element(By.ID, "Description").send_keys("this is description")
    time.sleep(5)
    driver.find_element(By.NAME, "save").click()
    time.sleep(5)

    driver.quit()


