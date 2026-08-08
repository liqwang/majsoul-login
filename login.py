import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


accounts = int(len(sys.argv[1:]) / 2)
print(f'Config {accounts} accounts')

for i in range(accounts):
    email = sys.argv[1 + i]
    passwd = sys.argv[1 + i + accounts]

    print('----------------------------')
    print(f'Account {i + 1}: starting browser...')

    # 1. Open browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://game.maj-soul.net/1/")
        print(f'Account {i + 1} loading game...')

        screen = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.TAG_NAME, "canvas"))
        )

        # Wait for login page / game resources to finish loading
        sleep(60)

        # 2. Input email
        ActionChains(driver) \
            .move_to_element_with_offset(screen, 350, -135) \
            .click() \
            .send_keys(email) \
            .perform()

        sleep(1)

        # 3. Input password
        ActionChains(driver) \
            .move_to_element_with_offset(screen, 350, -50) \
            .click() \
            .send_keys(passwd) \
            .perform()

        sleep(1)

        # 4. Login
        ActionChains(driver) \
            .move_to_element_with_offset(screen, 350, 60) \
            .click() \
            .perform()

        print(f'Account {i + 1} entering game...')

        # Wait for the game homepage to load after login
        sleep(25)

        # 5. Click the canvas once to trigger monthly-card reward collection
        # Click a relatively blank lower-left area rather than the center.
        ActionChains(driver) \
            .move_to_element_with_offset(screen, -450, 250) \
            .click() \
            .perform()

        print(f'Account {i + 1} clicked screen; waiting for reward collection...')

        # Keep browser open longer after clicking, so the reward request can complete.
        sleep(30)

        print(f'Account {i + 1} login and reward collection completed')

    except Exception as e:
        print(f'Account {i + 1} failed: {e}')

    finally:
        driver.quit()
        print(f'Account {i + 1} browser closed')
