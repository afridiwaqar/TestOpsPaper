import time
import subprocess
import psutil
import matplotlib.pyplot as plt
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
        email_field.send_keys('wix.mortal@gmail.com') 

        email_field.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the password field to appear

        password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        password_field.send_keys('password123') 

        password_field.send_keys(Keys.RETURN)
        time.sleep(10)  # Give it enough time to load after logging in

    finally:
        driver.quit()

def get_resource_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    return cpu_percent, memory_percent

if __name__ == '__main__':
    total_runs = 5  # Number of times to run the test
    cpu_usages = []
    memory_usages = []
    successes = []

    for i in range(total_runs):
        cpu_usage, memory_usage = get_resource_usage()
        cpu_usages.append(cpu_usage)
        memory_usages.append(memory_usage)

        try:
            test_gmail_login()
            successes.append(1)
        except Exception as e:
            print(f"Test failed: {e}")
            successes.append(0)

    avg_cpu_usage = sum(cpu_usages) / len(cpu_usages)
    avg_memory_usage = sum(memory_usages) / len(memory_usages)
    success_rates = [sum(successes[:i+1])/len(successes[:i+1])*100 for i in range(total_runs)]

    plt.figure(figsize=(12, 6))
    plt.bar(range(len(cpu_usages)), cpu_usages, align='center')
    plt.xticks(range(len(cpu_usages)), ['Run {}'.format(i+1) for i in range(len(cpu_usages))])
    plt.title('CPU Usage per Test Run')
    plt.xlabel('Run')
    plt.ylabel('CPU Usage (%)')
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.bar(range(len(memory_usages)), memory_usages, align='center')
    plt.xticks(range(len(memory_usages)), ['Run {}'.format(i+1) for i in range(len(memory_usages))])
    plt.title('Memory Usage per Test Run')
    plt.xlabel('Run')
    plt.ylabel('Memory Usage (%)')
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(range(len(success_rates)), success_rates)
    plt.title('Reliability Over Time')
    plt.xlabel('Run')
    plt.ylabel('Success Rate (%)')
    plt.grid(True)
    plt.show()

    print(f"Average CPU Usage: {avg_cpu_usage}%")
    print(f"Average Memory Usage: {avg_memory_usage}%")
    print(f"Overall Success Rate: {sum(successes)/len(successes)*100}%")
