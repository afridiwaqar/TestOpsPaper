from playwright.sync_api import sync_playwright
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_user_registration():
    with sync_playwright() as p:
        logging.info("Launching browser")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        logging.info("Navigating to the registration page")
        page.goto("http://localhost:5000/auth/register", timeout=60000)
        logging.info("Page loaded, checking for username input")

        try:
            page.wait_for_selector('input[name="username"]', state='visible', timeout=60000)
            logging.info("Username input found, filling the form")
            page.fill('input[name="name"]', "Test User1")
            page.fill('input[name="username"]', "testuser1")
            page.fill('input[name="email"]', "testuser1@example.com")
            page.fill('input[name="password"]', "Password123")
            page.fill('input[name="password2"]', "Password123")
            logging.info("Form filled, submitting")

            # Click the submit button
            page.wait_for_selector('button[type="submit"]', state='visible', timeout=60000)
            page.click('button[type="submit"]')
            logging.info("Form submitted, waiting for the success message")

            # Navigating to login page to check for the success message
            page.wait_for_url("http://localhost:5000/auth/login", timeout=60000)
            try:
                page.wait_for_selector('text="Confirm email sent, check your inbox."', timeout=60000)
                logging.info("Test passed")
            except Exception as e:
                logging.error(f"Success message not found: {e}")
                page.screenshot(path="success_message_not_found.png")
                with open("page_source.html", "w") as f:
                    f.write(page.content())
        except Exception as e:
            logging.error(f"Test failed: {e}")
            page.screenshot(path="error.png")
            with open("page_source.html", "w") as f:
                f.write(page.content())
        finally:
            browser.close()
            logging.info("Browser closed")

if __name__ == "__main__":
    start_time = time.time()
    test_user_registration()
    end_time = time.time()
    logging.info(f"Test duration: {end_time - start_time} seconds")
