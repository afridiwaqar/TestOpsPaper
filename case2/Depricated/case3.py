import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from appium import webdriver as appium_webdriver
from selenium.webdriver.chrome.options import Options

# Define capabilities
caps = {
    "platformName": "Windows",
    "browserName": "chrome",
    "goog:chromeOptions": {
        "args": ["--disable-gpu", "--no-sandbox", "--disable-dev-shm-usage", "--headless"]
    }
}

# Path to chromedriver executable
chromedriver_path = "C:/Users/afrid/Desktop/case2/chromeDriverWin64/chromedriver.exe"

# Initialize ChromeDriver service
service = Service(executable_path=chromedriver_path)

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")

# Initialize Appium WebDriver
try:
    driver = appium_webdriver.Remote(
        command_executor='http://127.0.0.1:4723',
        desired_capabilities=caps,
        options=chrome_options,
        service=service
    )
except Exception as e:
    print(f"Error initializing WebDriver: {str(e)}")
    driver = None

if driver:
    try:
        driver.get("http://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Appium")
        search_box.submit()
        time.sleep(5)  # Wait for search results to load
        print(driver.title)
    finally:
        driver.quit()
else:
    print("Test execution failed.")
