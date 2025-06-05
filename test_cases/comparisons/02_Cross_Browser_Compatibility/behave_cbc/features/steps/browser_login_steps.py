import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_browser(browser_name):
    if browser_name == "chrome":
        service = ChromeService(executable_path='/home/waqar/.wdm/drivers/chromedriver/linux64/125.0.6422.141/chromedriver-linux64/chromedriver')
        return webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FirefoxService(executable_path='/home/waqar/.wdm/drivers/geckodriver/linux64/v0.34.0/geckodriver')
        return webdriver.Firefox(service=service)
    elif browser_name == "edge":
        service = EdgeService(executable_path='/home/waqar/.wdm/drivers/edgedriver/linux64/125.0.2535.92/msedgedriver')
        return webdriver.Edge(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

@given('I open the browser "{browser}"')
def step_open_browser(context, browser):
    context.browser = get_browser(browser)
    context.start_time = time.time()

@when('I visit the login page')
def step_visit_login_page(context):
    context.browser.get("http://127.0.0.1:5000/auth/login")

@when('I enter the email "{email}"')
def step_enter_email(context, email):
    email_input = context.browser.find_element(By.ID, "email")
    email_input.send_keys(email)

@when('I enter the password "{password}"')
def step_enter_password(context, password):
    password_input = context.browser.find_element(By.ID, "password")
    password_input.send_keys(password)

@when('I submit the login form')
def step_submit_login_form(context):
    password_input = context.browser.find_element(By.ID, "password")
    password_input.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the next page to load

@then('I should see the title containing "{expected_title}"')
def step_verify_title(context, expected_title):
    title = context.browser.title
    assert expected_title in title, f"Expected '{expected_title}' in '{title}'"
    context.browser.quit()
    context.end_time = time.time()
    elapsed_time = context.end_time - context.start_time
    print(f"{context.browser.name} took {elapsed_time:.2f} seconds.")

