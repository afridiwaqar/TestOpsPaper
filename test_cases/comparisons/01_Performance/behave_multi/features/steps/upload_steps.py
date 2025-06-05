import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

@given('I open the browser')
def step_impl(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.start_time = time.time()  # Start timing

@given('I navigate to the login page')
def step_impl(context):
    context.driver.get("http://127.0.0.1:5000/auth/login")

@when('I fill in the login form')
def step_impl(context):
    context.driver.find_element(By.ID, 'email').send_keys('admin@helloflask.com')
    context.driver.find_element(By.ID, 'password').send_keys('helloflask')
    context.driver.find_element(By.ID, 'submit').click()

@then('I should be logged in')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(EC.invisibility_of_element((By.ID, 'email')))

@when('I upload files')
def step_impl(context):
    file_paths = [f'/media/waqar/databackups/Downloads/papers/Image_{i}.jpg' for i in range(1, 101)]

    for file_path in file_paths:
        context.driver.get("http://127.0.0.1:5000/upload")
        WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))
        file_input = context.driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
        file_input.send_keys(file_path)
        context.driver.find_element(By.CSS_SELECTOR, '.btn.btn-light.float-right').click()
        time.sleep(1)  # Adjust the timeout as needed

    context.end_time = time.time()
    context.execution_time = context.end_time - context.start_time

@then('the files should be uploaded successfully')
def step_impl(context):
    print(f"Execution Time: {context.execution_time} seconds")
    context.driver.quit()
