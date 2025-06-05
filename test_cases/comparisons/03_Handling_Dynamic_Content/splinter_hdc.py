from splinter import Browser
import time

def run():
    start_time = time.time()  # Start timing

    print("Starting Splinter script...")
    browser = Browser('chrome', headless=False)

    try:
        print("Navigating to the login page...")
        browser.visit("http://127.0.0.1:5000/auth/login")

        print("Filling in the login form...")
        browser.fill('email', 'admin@helloflask.com')
        browser.fill('password', 'helloflask')

        submit_button = browser.find_by_name('submit')
        if submit_button:
            print("Submit button found, clicking...")
            submit_button.click()
        else:
            print("Submit button not found!")
            return

        print("Navigating to the page with comments...")
        browser.visit("http://127.0.0.1:5000/photo/34")
        print("Waiting for the comments section to load...")
        browser.is_element_present_by_css('div.comments', wait_time=20)

        initial_comments_text = browser.find_by_css('div.comments h3').text
        print(f"Initial number of comments: {initial_comments_text}")

        browser.fill('body', 'This is a test comment.')

        submit_button = browser.find_by_name('submit')
        if submit_button:
            print("Submit button found, clicking...")
            submit_button.click()
        else:
            print("Submit button not found!")
            return

        print("Waiting for the new comment to appear...")
        time.sleep(1)  # Wait for 5 seconds

        updated_comments_text = browser.find_by_css('div.comments h3').text
        print(f"Updated number of comments: {updated_comments_text}")

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time} seconds")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

    finally:
        print("Closing the browser...")
        browser.quit()

run()
