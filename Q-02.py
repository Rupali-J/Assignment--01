# 2. Login with Invalid Credentials & Verify Error Message

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
    driver.find_element(By.ID, "username").send_keys("Org@360dc.com")
    driver.find_element(By.ID, "password").send_keys("Ru@1996")
    driver.find_element(By.ID, "Login").click()
    time.sleep(7)
    exp_error_msg = "Please check your username and password. If you still can't log in, contact your Salesforce " \
                    "administrator. "

    error_msg_actual = driver.find_element(By.XPATH, "//div[@id='error']").text
    print("Error message is: ", error_msg_actual)

    if exp_error_msg == error_msg_actual:
        assert True
