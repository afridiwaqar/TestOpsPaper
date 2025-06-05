from appium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def benchmark_appium():
    # Set up the Chrome options
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')  # Run in headless mode if needed

    # Prepare the capabilities
    capabilities = {
        'platformName': 'Windows',
        'automationName': 'Chromium',
        'browserName': 'Chrome',
        'goog:chromeOptions': chrome_options.to_capabilities()['goog:chromeOptions'],
    }

    try:
        # Start the WebDriver session
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=capabilities
        )
    except Exception as e:
        print(f"Error initializing WebDriver: {e}")
        return

    results = {}

    try:
        # Home Page Load Time
        start_time = time.time()
        driver.get('http://127.0.0.1:5000/')
        results['home_load_time'] = time.time() - start_time

        # Navigate to Register Page and Measure Load Time
        start_time = time.time()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register'))).click()
        results['register_page_load_time'] = time.time() - start_time

        # Fill Registration Form and Measure Submission Time
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys('testuser')
        driver.find_element(By.ID, 'email').send_keys('testuser@example.com')
        driver.find_element(By.ID, 'password').send_keys('password')
        start_time = time.time()
        driver.find_element(By.TAG_NAME, 'button').click()
        results['register_submit_time'] = time.time() - start_time

        # Navigate to Login Page and Measure Load Time
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))).click()
        start_time = time.time()
        results['login_page_load_time'] = time.time() - start_time

        # Fill Login Form and Measure Submission Time
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'username'))).send_keys('testuser')
        driver.find_element(By.ID, 'password').send_keys('password')
        start_time = time.time()
        driver.find_element(By.TAG_NAME, 'button').click()
        results['login_submit_time'] = time.time() - start_time

        # Measure Logout Time
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Logout'))).click()
        results['logout_time'] = time.time() - start_time

    except Exception as e:
        print(f"Error during test execution: {e}")
    finally:
        driver.quit()

    return results

if __name__ == "__main__":
    results = benchmark_appium()
    if results:
        print(results)
    else:
        print("Test execution failed.")
