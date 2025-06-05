import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def test_login(browser_name):
    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif browser_name == "edge":
        service = EdgeService(EdgeChromiumDriverManager().install())
        options = EdgeOptions()
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError("Unsupported browser: " + browser_name)
    
    start_time = time.time()
    try:
        driver.get("http://127.0.0.1:5000/auth/login")

        email_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "password")

        email_input.send_keys("admin@helloflask.com")
        password_input.send_keys("helloflask")
        password_input.send_keys(Keys.RETURN)

        time.sleep(2)

        assert "Home - Albumy" in driver.title or "Dashboard" in driver.title
        
        logger.info(f"{browser_name}: Login successful")

    except Exception as e:
        logger.error(f"{browser_name}: Login failed - {e}")
    
    finally:
        driver.quit()
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"{browser_name}: Test completed in {duration:.2f} seconds")

if __name__ == "__main__":
    browsers = ["chrome", "firefox", "edge"]
    for browser in browsers:
        test_login(browser)

