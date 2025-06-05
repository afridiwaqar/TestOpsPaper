from playwright.sync_api import sync_playwright
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def test_upload_profile_picture():
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
            page.wait_for_selector('text="Confirm email sent, check your inbox."', timeout=60000)
            logging.info("Login successful, navigating to profile settings")

            # Navigate to profile settings
            page.goto("http://localhost:5000/user/settings/profile", timeout=60000)
            logging.info("Profile settings page loaded, checking for upload input")

            # Navigate to avatar settings
            page.goto("http://localhost:5000/user/settings/avatar", timeout=60000)
            logging.info("Avatar settings page loaded, checking for upload input")

            # Upload profile picture
            page.wait_for_selector('input[type="file"]', state='visible', timeout=60000)
            page.set_input_files('input[type="file"]', r'C:\Users\afrid\Documents\FAST\TestOps\test_cases\playwrite\mypic.jpg')
            logging.info("Profile picture uploaded, submitting form")

            # Submit the form
            page.click('button[type="submit"]')
            logging.info("Form submitted, checking for success message")

            # Check for upload success
            page.wait_for_selector('text="Profile updated successfully"', timeout=60000)
            logging.info("Profile picture upload successful, test passed")
        except Exception as e:
            logging.error(f"Test failed: {e}")
            page.screenshot(path="upload_error.png")
            with open("upload_page_source.html", "w") as f:
                f.write(page.content())
        finally:
            browser.close()
            logging.info("Browser closed")

if __name__ == "__main__":
    start_time = time.time()
    test_upload_profile_picture()
    end_time = time.time()
    logging.info(f"Test duration: {end_time - start_time} seconds")
