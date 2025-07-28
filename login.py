import sys
import time
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def main():
    start_time = time.time()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    success = False
    
    try:
        acccounts = int(len(sys.argv[1:])/2)
        print(f'Config {acccounts} accounts')
        for i in range(acccounts):
            email = sys.argv[1+i]
            passwd = sys.argv[1+i+acccounts]
            print('----------------------------')

            #1.open browser
            options = webdriver.ChromeOptions()
            options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
            driver.set_window_size(1000, 720)
            driver.get("https://game.maj-soul.net/1/")
            print(f'Account {i+1} loading game...')
            sleep(20)

            #2.input email
            screen = driver.find_element(By.ID, 'layaCanvas')
            ActionChains(driver)\
                .move_to_element_with_offset(screen, 250, -100)\
                .click()\
                .perform()
            driver.find_element(By.NAME, 'input').send_keys(email)
            print('Input email successfully')

            #3.input password
            ActionChains(driver)\
                .move_to_element_with_offset(screen, 250, -50)\
                .click()\
                .perform()
            driver.find_element(By.NAME, 'input_password').send_keys(passwd)
            print('Input password successfully')

            #4.login
            ActionChains(driver)\
                .move_to_element_with_offset(screen, 250, 50)\
                .click()\
                .perform()
            print('Entering game...')
            sleep(20) #loading...
            print('Login success')
            driver.quit()
        
        success = True
        
    except Exception as e:
        print(f'Login failed: {str(e)}')
        success = False
    
    finally:
        # 记录执行日志
        end_time = time.time()
        execution_time = end_time - start_time
        
        with open("log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"{current_time}-{'Success' if success else 'Failed'}-{execution_time:.2f}s\n")
        
        print(f"Execution completed. Status: {'Success' if success else 'Failed'}, Time: {execution_time:.2f}s")


if __name__ == "__main__":
    main()
