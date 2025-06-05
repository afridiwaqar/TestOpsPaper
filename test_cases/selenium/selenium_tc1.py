from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver_path = '/usr/local/bin/chromedriver' 

def test_gmail_login():
    chrome_options = webdriver.ChromeOptions()
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get('https://accounts.google.com/signin')

        email_field = driver.find_element(By.NAME, 'identifier')
        email_field.send_keys('afridi.waqar@gmail.com') 


        email_field.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the password field to appear

        wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

        password_field.send_keys('password123')  

        password_field.send_keys(Keys.RETURN)
        time.sleep(10)  

    finally:
        driver.quit()

if __name__ == '__main__':
    test_gmail_login()
