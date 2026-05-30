import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

acccounts = int(len(sys.argv[1:])/2)
print(f'Config {acccounts} accounts')
for i in range(acccounts):
    email = sys.argv[1+i]
    passwd = sys.argv[1+i+acccounts]
    print('----------------------------')

    #1.open browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i+1} loading game...')

    try:
        screen = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, "canvas"))
        )
    except:
        driver.quit()
        raise

    sleep(60)

    #2.input email
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 350, -135)\
        .click()\
        .perform()
    sleep(1)
    ActionChains(driver)\
        .send_keys(email)\
        .perform()
    sleep(1)

    #3.input password
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 350, -50)\
        .click()\
        .perform()
    sleep(1)
    ActionChains(driver)\
        .send_keys(passwd)\
        .perform()
    sleep(1)

    #4.login
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 350, 60)\
        .click()\
        .perform()
    print(f'Account {i+1} entering game...')
    sleep(20)  # loading...
    print(f'Account {i+1} login completed')

    driver.quit()
