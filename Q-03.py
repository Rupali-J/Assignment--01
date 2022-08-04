# 3. After Login switch lightning to classic and classic to lightning
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

    # classic to lightning
    time.sleep(7)
    driver.find_element(By.XPATH, '//a[contains(@href,"SwitchToLightningClick")]').click()

    # lightning to classic
    time.sleep(8)
    driver.find_element(By.XPATH, '//span[contains(@class,"uiImage")]').click()

    time.sleep(6)
    driver.find_element(By.XPATH, '//a[contains(@href,"destination=classic")]').click()

    time.sleep(15)
    driver.quit()
