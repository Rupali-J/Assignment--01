# Goto Account And Add One New Account Record.
# Goto Account Delete Added Account Record.
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--disable-notifications")
option.add_argument("start-maximized")
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, chrome_options=option)
driver.get("https://login.salesforce.com")

expected_title = "Login | Salesforce"
actual_title = driver.title

if expected_title == actual_title:
    assert True
    main_page1 = driver.current_window_handle
    driver.find_element(By.ID, "username").send_keys("OrgRup@360dc.com")
    driver.find_element(By.ID, "password").send_keys("Rupali@300196")
    driver.find_element(By.ID, "Login").click()

    time.sleep(6)
    # popup handling
    for handle in driver.window_handles:
        if handle != main_page1:
            driver.find_element(By.ID, "tryLexDialogX").click()
        else:
            print("no popup displays")
    # switching between classic and lightning
    url = driver.current_url
    web = "https://360dc50-dev-ed.lightning.force.com/lightning/page/home"
    time.sleep(7)
    if web != url:
        driver.find_element(By.XPATH, '//a[contains(@href,"SwitchToLightningClick")]').click()
    else:
        print("on lightning")

    # CLICK ON ACCOUNT OBJECT TAB
    driver.find_element(By.XPATH, "(//one-app-nav-bar-item-root[@data-assistive-id='operationId'])[6]").click()
    time.sleep(7)

    # click on new button to create account record
    driver.find_element(By.XPATH, "//a[@title = 'New']").click()
    time.sleep(7)
    # ENTER NAME and click on save
    driver.find_element(By.XPATH, "(//input[@class= 'slds-input'])[2]").send_keys("Tester")
    time.sleep(7)
    driver.find_element(By.XPATH, "//li//lightning-button//button[@class='slds-button slds-button_brand']").click()
    print("New account created successfully....")
    time.sleep(10)
    # click on dropdown button to delete the record
    driver.find_element(By.XPATH,
                        "//li//lightning-button-menu//button[@class= 'slds-button slds-button_icon-border-filled']").click()
    time.sleep(7)
    # click on delete
    driver.find_element(By.XPATH, "//runtime_platform_actions-ribbon-menu-item//a//span[text() = 'Delete']").click()
    time.sleep(7)
    driver.find_element(By.XPATH, "//button//span[text()= 'Delete']").click()
    print("account deleted successfully")
    time.sleep(7)
