import time
from playwright.sync_api import sync_playwright

def run(playwright):
    start_time = time.time()  # Start timing

    browser = playwright.chromium.launch(headless=False)  # Set headless=False if you want to see the browser actions
    page = browser.new_page()
    page.goto("http://localhost:5000/upload")  # Updte the URL to your Albumy application
    browser.close()

    end_time = time.time()  # End timing
    execution_time = end_time - start_time

    print(f"Execution Time: {execution_time} seconds")

with sync_playwright() as p:
    run(p)
