from playwright.sync_api import sync_playwright
import time

def run(playwright):
    start_time = time.time()  # Capture the start time

    browser = playwright.chromium.launch(headless=False)  # Set headless=False if you want to see the browser actions
    page = browser.new_page()
    
    # Navigate to the registration page
    page.goto("http://127.0.0.1:5000/auth/register")
    
    # Fill out the registration form
    page.fill('input#name', 'Waqar Afridi')  # Fill in the Name field
    page.fill('input#email', 'afridi.waqar@gmail.com')
    page.fill('input#username', 'waqar')
    page.fill('input#password', 'khan1234')
    page.fill('input#password2', 'khan1234')
    
    # Find a reliable way to click the submit button
    # Since the submit button lacks a unique identifier, we'll target it by its position in the DOM
    # This approach might need adjustment depending on the actual layout and elements present
    page.click('input.btn.btn-secondary[type="submit"]')
    
    # Introduce a delay to allow for navigation to occur after submission
    page.wait_for_timeout(3000)  # Wait for 3 seconds
    
    # Navigate to the login page and measure the time taken
    start_time_login = page.evaluate('''() => {
        const startTime = performance.now();
        window.location.href = "/auth/login";
        return performance.now() - startTime;
    }''')
    
    # Print the time taken for navigation
    print(f"Time taken to navigate to login page: {start_time_login} ms")
    
    # Close the browser
    browser.close()

    end_time = time.time()  # Capture the end time
    execution_time = end_time - start_time  # Calculate the execution time
    print(f"Total Execution Time: {execution_time} seconds")

with sync_playwright() as p:
    run(p)

