from playwright.sync_api import sync_playwright
from webdriver_manager.chrome import ChromeDriverManager
import time

def run(playwright):
    start_time = time.time()  # Start timing

    print("Starting Playwright script...")
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        print("Navigating to the login page...")
        page.goto("http://127.0.0.1:5000/auth/login")

        print("Filling in the login form...")
        page.fill('#email', 'admin@helloflask.com')
        page.fill('#password', 'helloflask')
        page.click('#submit')

        print("Navigating to the page with comments...")
        page.goto("http://127.0.0.1:5000/photo/39")

        print("Waiting for the comments section to load...")
        page.wait_for_selector('#comments')

        initial_comments_text = page.inner_text('#comments h3')
        print(f"Initial number of comments: {initial_comments_text}")

        page.fill('#body', 'This is a test comment.')

        page.click('#submit')

        print("Waiting for the new comment to appear...")
        page.wait_for_timeout(5000)  # Wait for 5 seconds

        updated_comments_text = page.inner_text('#comments h3')
        print(f"Updated number of comments: {updated_comments_text}")

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

    finally:
        print("Closing the browser...")
        browser.close()

with sync_playwright() as p:
    run(p)

