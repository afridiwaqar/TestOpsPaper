import time
import logging
import csv
import os
from splinter import Browser

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

csv_file = 'test_results_splinter.csv'
csv_columns = ['Browser', 'Status', 'Duration']

def log_to_csv(data):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def test_login(browser_name):
    if browser_name == "chrome":
        browser = Browser('chrome')
    elif browser_name == "firefox":
        browser = Browser('firefox')
    elif browser_name == "edge":
        browser = Browser('edge')
    else:
        raise ValueError("Unsupported browser: " + browser_name)
    
    start_time = time.time()
    try:
        browser.visit("http://127.0.0.1:5000/auth/login")

        browser.fill('email', 'admin@helloflask.com')
        browser.fill('password', 'helloflask')
        browser.find_by_id('submit').click()

        browser.is_element_not_present_by_id('email', wait_time=10)

        title = browser.title
        assert "Home - Albumy" in title or "Dashboard" in title

        status = "Success"
        logger.info(f"{browser_name}: Login successful")

    except Exception as e:
        status = "Failed"
        logger.error(f"{browser_name}: Login failed - {e}")
    
    finally:
        browser.quit()
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"{browser_name}: Test completed in {duration:.2f} seconds")
        
        log_to_csv({
            'Browser': browser_name,
            'Status': status,
            'Duration': f"{duration:.2f} seconds"
        })

if __name__ == "__main__":
    browsers = ["chrome", "firefox", "edge"]
    for browser in browsers:
        test_login(browser)

