import time
import logging
import csv
import os
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

csv_file = 'test_results_playwright.csv'
csv_columns = ['Browser', 'Status', 'Duration']

def log_to_csv(data):
    file_exists = os.path.isfile(csv_file)
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=csv_columns)
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def test_login(playwright, browser_name):
    if browser_name == "chrome":
        browser = playwright.chromium.launch(executable_path='/usr/bin/google-chrome-stable')
    elif browser_name == "firefox":
        browser = playwright.firefox.launch()
    elif browser_name == "edge":
        browser = playwright.chromium.launch(executable_path='/usr/bin/microsoft-edge-stable')
    else:
        raise ValueError("Unsupported browser: " + browser_name)
    
    start_time = time.time()
    try:
        context = browser.new_context()
        page = context.new_page()
        page.goto("http://127.0.0.1:5000/auth/login")

        page.fill("input#email", "admin@helloflask.com")
        page.fill("input#password", "helloflask")
        page.press("input#password", "Enter")

        time.sleep(2)

        title = page.title()
        assert "Home - Albumy" in title or "Dashboard" in title

        status = "Success"
        logger.info(f"{browser_name}: Login successful")

    except Exception as e:
        status = "Failed"
        logger.error(f"{browser_name}: Login failed - {e}")
    
    finally:
        browser.close()
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"{browser_name}: Test completed in {duration:.2f} seconds")
        
        log_to_csv({
            'Browser': browser_name,
            'Status': status,
            'Duration': f"{duration:.2f} seconds"
        })

if __name__ == "__main__":
    with sync_playwright() as playwright:
        browsers = ["chrome", "firefox", "edge"]
        for browser in browsers:
            test_login(playwright, browser)

