import time
from playwright.sync_api import sync_playwright

def run(playwright):
    start_time = time.time()  # Start timing

    browser = playwright.chromium.launch(headless=False)  # Set headless=False if you want to see the browser actions
    page = browser.new_page()
    
    # Navigate to the login page
    page.goto("http://127.0.0.1:5000/auth/login")
    
    # Fill in the login form
    page.fill('input[id=email]', 'admin@helloflask.com')
    page.fill('input[id=password]', 'helloflask')
    page.click('input[id=submit]')
    
    # Wait for the email input field to disappear, indicating the login form has been submitted
    page.wait_for_selector('input[id=email]', state="detached")
    
    # Now navigate to the upload page
    page.goto("http://127.0.0.1:5000/upload")
    
    # Ensure the page has loaded
    page.wait_for_load_state("networkidle")
    
    
    page.set_input_files('input[type="file"]', ['/home/waqar/FAST/TestOps/test_cases/playwrite/working_flawlessly/image.jpg'])
    
    # Click the "Done" button
    page.click('.btn.btn-light.float-right')
    
    # Wait for the upload to complete or for a specific element to indicate success
    page.wait_for_timeout(5000)  # Adjust the timeout as needed
    
    # End timing
    end_time = time.time()
    execution_time = end_time - start_time
    
    print(f"Execution Time: {execution_time} seconds")

    # Close the browser
    browser.close()

with sync_playwright() as p:
    run(p)

