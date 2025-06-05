import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run():
    start_time = time.time()  # Start timing

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("http://127.0.0.1:5000/auth/login")

        driver.find_element(By.ID, 'email').send_keys('admin@helloflask.com')
        driver.find_element(By.ID, 'password').send_keys('helloflask')
        driver.find_element(By.ID, 'submit').click()

        WebDriverWait(driver, 10).until(EC.invisibility_of_element((By.ID, 'email')))

        driver.get("http://127.0.0.1:5000/upload")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))

        file_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys('/home/waqar/FAST/TestOps/test_cases/playwrite/working_flawlessly/image.jpg')

        driver.find_element(By.CSS_SELECTOR, '.btn.btn-light.float-right').click()

        time.sleep(5)  # Adjust the timeout as needed

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time} seconds")

    finally:
        driver.quit()

run()

