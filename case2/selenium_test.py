# selenium_test.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def user_registration_and_login(driver):
    # Step 1: Navigate to the registration page
    driver.get('http://127.0.0.1:5000/register')
    
    # Step 2: Fill out the registration form
    driver.find_element(By.ID, 'username').send_keys('testuser')
    driver.find_element(By.ID, 'email').send_keys('testuser@example.com')
    driver.find_element(By.ID, 'password').send_keys('password')
    
    # Step 3: Submit the registration form
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Step 4: Verify registration success
    time.sleep(3)  # wait for the page to load
    assert 'Registration successful!' in driver.page_source
    
    # Step 5: Navigate to the login page
    driver.get('http://127.0.0.1:5000/login')
    
    # Step 6: Enter the username and password
    driver.find_element(By.ID, 'username').send_keys('testuser')
    driver.find_element(By.ID, 'password').send_keys('password')
    
    # Step 7: Submit the login form
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    
    # Step 8: Verify login success
    time.sleep(3)  # wait for the page to load
    assert 'Welcome testuser!' in driver.page_source

# Setup
driver = webdriver.Chrome()
try:
    user_registration_and_login(driver)
finally:
    driver.quit()

