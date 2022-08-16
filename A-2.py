# Open Sales App And Verify URL
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

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

    app = "Sales"
    exp_app = driver.find_element(By.XPATH, "(//span[text() = 'Service'])[3]").text
    time.sleep(7)
    if app != exp_app:
        # click on app launcher and type sales in search box
        driver.find_element(By.XPATH, "//div[@class= 'appLauncher slds-context-bar__icon-action']//button[@class= 'slds-button slds-show']").click()
        time.sleep(7)
        # enter sales in search box
        driver.find_element(By.XPATH, "//div[@class='container']//input[@id='input-91']").send_keys("Sales")
        time.sleep(7)
        # click on sales
        driver.find_element(By.XPATH, "(//lightning-formatted-rich-text//span//p//b)[3]").click()
        print("now u are on sales")
        time.sleep(7)
    else:
        print("you are already on sales app")
        time.sleep(7)
    # verify URL of the page
    exp_url = "https://360dc50-dev-ed.lightning.force.com/lightning/page/home"
    actual_url = driver.current_url
    if exp_url == actual_url:
        print("The current url is:" + actual_url)
    else:
        print("No URL matches")
    driver.quit()
    