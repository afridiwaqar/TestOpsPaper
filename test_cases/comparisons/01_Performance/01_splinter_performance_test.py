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

        browser.find_by_css('input[type="file"]').first.type('/home/waqar/FAST/TestOps/test_cases/playwrite/working_flawlessly/image.jpg')

        browser.find_by_css('.btn.btn-light.float-right').click()

        time.sleep(5)  # Adjust the timeout as needed

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time} seconds")

run()

