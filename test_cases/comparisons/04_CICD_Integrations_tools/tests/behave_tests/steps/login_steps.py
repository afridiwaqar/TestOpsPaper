from behave import *
from selenium import webdriver

@given('I open the browser "{browser}"')
def step_open_browser(context, browser):
    if browser == "chrome":
        context.driver = webdriver.Chrome()
    elif browser == "firefox":
        context.driver = webdriver.Firefox()
    elif browser == "edge":
        context.driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

@when('I visit the login page')
def step_visit_login_page(context):
    context.driver.get("http://127.0.0.1:5000/auth/login")

@when('I enter the email "{email}"')
def step_enter_email(context, email):
    context.driver.find_element_by_name("email").send_keys(email)

@when('I enter the password "{password}"')
def step_enter_password(context, password):
    context.driver.find_element_by_name("password").send_keys(password)

@when('I submit the login form')
def step_submit_login_form(context):
    context.driver.find_element_by_name("submit").click()

@then('I should see the title containing "{text}"')
def step_check_title(context, text):
    assert text in context.driver.title
    context.driver.quit()
