import time
from playwright.sync_api import sync_playwright

def run(playwright):
    start_time = time.time()  # Start timing

    browser = playwright.chromium.launch(headless=False)  # Set headless=False if you want to see the browser actions
    page = browser.new_page()
    
    page.goto("http://127.0.0.1:5000/auth/login")
    
    page.fill('input[id=email]', 'admin@helloflask.com')
    page.fill('input[id=password]', 'helloflask')
    page.click('input[id=submit]')
    
    page.wait_for_selector('input[id=email]', state="detached")
    Print "Hello"
    
    
    
    image_paths = [f'/media/waqar/databackups/Downloads/papers/Image_{i}.jpg' for i in range(1, 101)]

    for image_path in image_paths:
        print(image_path)
        page.goto("http://127.0.0.1:5000/upload")
		
        page.wait_for_load_state("networkidle")
        page.set_input_files('input[type="file"]', image_path)
        page.click('.btn.btn-light.float-right')
        
        page.wait_for_timeout(1)  # Adjust the timeout as needed
        
    end_time = time.time()
    execution_time = end_time - start_time
        
    print(f"Execution Time: {execution_time} seconds")

    browser.close()

with sync_playwright() as p:
    run(p)
