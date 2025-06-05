import time
import subprocess
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = '/usr/local/bin/chromedriver'

def test_gmail_login():
    chrome_options = webdriver.ChromeOptions()
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get('https://accounts.google.com/signin')

        email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'identifier')))
        email_field.send_keys('afridi.waqar@gmail.com')  

        email_field.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the password field to appear

        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_field.send_keys('password') 

        password_field.send_keys(Keys.RETURN)
        time.sleep(10)  # Give it enough time to load after logging in

    finally:
        driver.quit()

if __name__ == '__main__':
    start_time = time.time()

    success_count = 0
    total_runs = 2  # Number of times to run the test

    for _ in range(total_runs):
        try:
            test_gmail_login()
            success_count += 1
        except Exception as e:
            print(f"Test failed: {e}")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time} seconds")

    print(f"Success rate: {success_count / total_runs * 100}%")

    cpu_usage = subprocess.check_output(['top', '-bn1']).decode('utf-8').split('\n')[1].strip().split()[1]
    mem_usage = subprocess.check_output(['free', '-m']).decode('utf-8').split('\n')[1].strip().split()[1]

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {mem_usage}MB")
