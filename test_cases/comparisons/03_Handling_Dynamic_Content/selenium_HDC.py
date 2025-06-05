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

        WebDriverWait(driver, 10).until(EC.url_changes("http://127.0.0.1:5000/auth/login"))

        driver.get("http://127.0.0.1:5000/photo/39")  # Adjust the URL as needed

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'comments')))

        initial_comments_text = driver.find_element(By.CSS_SELECTOR, '#comments h3').text
        print(f"Initial number of comments: {initial_comments_text}")

        comment_box = driver.find_element(By.ID, 'body')
        comment_box.send_keys('This is a test comment.')

        driver.find_element(By.ID, 'submit').click()

        WebDriverWait(driver, 10).until(
            lambda d: '4 Comments' in d.find_element(By.CSS_SELECTOR, '#comments h3').text
        )

        updated_comments_text = driver.find_element(By.CSS_SELECTOR, '#comments h3').text
        print(f"Updated number of comments: {updated_comments_text}")

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")

    finally:
        driver.quit()

run()

