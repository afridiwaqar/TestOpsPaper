from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import psutil

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
# Uncomment the next line if you want to run headlessly
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Set capabilities for using the Chromium driver
chrome_options.set_capability("browserName", "chromium")
# Remove the following lines as they are not applicable
chrome_options.set_capability("platformName", "Linux")
chrome_options.set_capability("automationName", "uiac")

driver = webdriver.Remote('http://localhost:4723', options=chrome_options)

# Benchmarking script
def benchmark_flask_app():
    process = psutil.Process()
    
    # Open the Flask web application
    driver.get('http://localhost:5000')
    start_time = time.time()
    
    # Register a new user
    driver.get('http://localhost:5000/register')
    time.sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'email').send_keys('testuser@example.com')
    driver.find_element(By.NAME, 'password').send_keys('password')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    
    # Log in with the registered user
    driver.get('http://localhost:5000/login')
    time.sleep(1)
    driver.find_element(By.NAME, 'username').send_keys('testuser')
    driver.find_element(By.NAME, 'password').send_keys('password')
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(1)
    
    # Retrieve user information
    driver.get('http://localhost:5000/user_info')
    time.sleep(1)
    
    end_time = time.time()
    execution_time = end_time - start_time
    memory_info = process.memory_info()
    
    print(f"Test execution time: {execution_time} seconds")
    print(f"Memory usage: {memory_info.rss / (1024 ** 2)} MB")
    
    driver.quit()

if __name__ == "__main__":
    benchmark_flask_app()

