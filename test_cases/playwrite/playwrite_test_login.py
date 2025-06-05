from playwright.sync_api import sync_playwright
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_user_login():
    with sync_playwright() as p:
        logging.info("Launching browser")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        logging.info("Navigating to the login page")
        page.goto("http://localhost:5000/auth/login", timeout=60000)
        logging.info("Page loaded, checking for email input")

        try:
            page.wait_for_selector('input[name="email"]', state='visible', timeout=60000)
            logging.info("Email input found, filling the form")
            page.fill('input[name="email"]', "testuser@example.com")
            page.fill('input[name="password"]', "Password123")
            logging.info("Form filled, submitting")

            # Click the submit button
            page.wait_for_selector('button[type="submit"]', state='visible', timeout=60000)
            page.click('button[type="submit"]')
            logging.info("Form submitted, checking for success message")

            # Check for successful login
            page.wait_for_selector('text="Login success."', timeout=60000)
            logging.info("Login successful, test passed")
        except Exception as e:
            logging.error(f"Test failed: {e}")
            page.screenshot(path="login_error.png")
            with open("login_page_source.html", "w") as f:
                f.write(page.content())
        finally:
            browser.close()
            logging.info("Browser closed")

if __name__ == "__main__":
    start_time = time.time()
    test_user_login()
    end_time = time.time()
    logging.info(f"Test duration: {end_time - start_time} seconds")
