# Create Test Script For Custom Object To Delete

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
    driver.find_element(By.ID, "password").send_keys("Rupali@300196")
    driver.find_element(By.ID, "Login").click()

    time.sleep(6)
    # close dialog box
    driver.find_element(By.ID, "tryLexDialogX").click()

    time.sleep(7)
    # click on setup
    driver.find_element(By.XPATH, "//a[@id='setupLink']").click()

    time.sleep(5)
    # CLICK ON CREATE OPTION BELOW QUICK FIND BOX
    driver.find_element(By.ID, "DevTools_font").click()
    # CLICK ON OBJECTS INSIDE CREATE
    driver.find_element(By.ID, "CustomObjects_font").click()
    # verify custom object is visible
    obj = driver.find_element(By.LINK_TEXT, "AutoObject")
    obj_status = obj.is_displayed()
    if obj_status:
        obj.click()
        time.sleep(5)
        driver.find_element(By.NAME, "del").click()
        # changing the handles to access confirm page
        for handle in driver.window_handles:
            if handle != main_page1:
                cnf_page = handle
            # change the control to confirm page
                driver.switch_to.window(cnf_page)

            # click on checkbox
                driver.find_element(By.ID, "confirmed").click()
            # click on delete button
                driver.find_element(By.NAME, "del").click()
    else:
        assert False
