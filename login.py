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
        print(f'Canvas found, size: {screen.size}')
    except:
        driver.save_screenshot(f"error_canvas_{i+1}.png")
        driver.quit()
        raise
    
    print('Waiting for game to fully load...')
    sleep(60)
    print('Game load wait completed')
    
    driver.save_screenshot(f"login_screen_{i+1}.png")
    print('Login screen captured')

    print('Trying to input email...')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 750, 180)\
        .click()\
        .perform()
    sleep(1)
    ActionChains(driver)\
        .send_keys(email)\
        .perform()
    sleep(2)
    print('Email input attempted')

    driver.save_screenshot(f"after_email_{i+1}.png")
    print('After email input captured')

    print('Trying to input password...')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 750, 240)\
        .click()\
        .perform()
    sleep(1)
    ActionChains(driver)\
        .send_keys(passwd)\
        .perform()
    sleep(2)
    print('Password input attempted')

    driver.save_screenshot(f"after_password_{i+1}.png")
    print('After password input captured')

    print('Clicking login button...')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 750, 340)\
        .click()\
        .perform()
    print('Login button clicked')
    sleep(15)
    
    driver.save_screenshot(f"after_login_click_{i+1}.png")
    print('After login click captured')

    print('Waiting for login process...')
    sleep(45)
    
    driver.save_screenshot(f"after_login_wait_{i+1}.png")
    print('After login wait captured')

    print('Checking for server selection...')
    sleep(5)
    
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 750, 100)\
        .click()\
        .perform()
    sleep(5)

    driver.save_screenshot(f"after_server_select_{i+1}.png")
    print('After server select captured')

    print('Waiting for game entry...')
    sleep(30)

    print('Attempting to claim monthly card...')
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 0, 50)\
        .click()\
        .perform()
    sleep(3)
    
    ActionChains(driver)\
        .move_to_element_with_offset(screen, 0, 50)\
        .click()\
        .perform()
    sleep(3)
    
    print('Monthly card claim attempt completed')
    
    driver.save_screenshot(f"result_{i+1}.png")
    print(f'Screenshot saved as result_{i+1}.png')
    
    driver.quit()