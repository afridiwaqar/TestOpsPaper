import time
from splinter import Browser

def run():
    start_time = time.time()  # Start timing

    with Browser('chrome', headless=False) as browser:
        browser.visit("http://127.0.0.1:5000/auth/login")

        browser.fill('email', 'admin@helloflask.com')
        browser.fill('password', 'helloflask')
        browser.find_by_id('submit').click()

        browser.is_element_not_present_by_id('email', wait_time=10)

        browser.visit("http://127.0.0.1:5000/upload")

        browser.is_element_present_by_css('input[type="file"]', wait_time=10)

        image_paths = [f'/media/waqar/databackups/Downloads/papers/Image_{i}.jpg' for i in range(1, 101)]

        for image_path in image_paths:
            file_input = browser.find_by_css('input[type="file"]').first
            file_input.type(image_path)

            browser.find_by_css('.btn.btn-light.float-right').click()

            time.sleep(1)  # Adjust the timeout as needed

            browser.visit("http://127.0.0.1:5000/upload")
            browser.is_element_present_by_css('input[type="file"]', wait_time=10)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time} seconds")

run()

