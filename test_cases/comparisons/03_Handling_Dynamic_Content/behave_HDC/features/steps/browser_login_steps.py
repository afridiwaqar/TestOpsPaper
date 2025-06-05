from behave import given, when, then
from splinter import Browser
import time

@given('I open the browser "{browser_name}"')
def step_open_browser(context, browser_name):
    context.browser = Browser(browser_name, headless=False)
    context.start_time = time.time()  # Start timing

@when('I visit the login page')
def step_visit_login_page(context):
    context.browser.visit("http://127.0.0.1:5000/auth/login")

@when('I fill in the login form with email "{email}" and password "{password}"')
def step_fill_login_form(context, email, password):
    context.browser.fill('email', email)
    context.browser.fill('password', password)

@when('I submit the login form')
def step_submit_login_form(context):
    submit_button = context.browser.find_by_name('submit')
    if submit_button:
        submit_button.click()
    else:
        raise Exception("Submit button not found!")

@when('I navigate to the photo page with id "{photo_id}"')
def step_navigate_to_photo_page(context, photo_id):
    context.browser.visit(f"http://127.0.0.1:5000/photo/{photo_id}")
    context.browser.is_element_present_by_css('div.comments', wait_time=20)

@then('I should see the initial number of comments')
def step_see_initial_comments(context):
    initial_comments_text = context.browser.find_by_css('div.comments h3').text
    context.initial_comments_text = initial_comments_text
    print(f"Initial number of comments: {initial_comments_text}")

@when('I enter a new comment "{comment}"')
def step_enter_new_comment(context, comment):
    context.browser.fill('body', comment)

@when('I submit the comment form')
def step_submit_comment_form(context):
    submit_button = context.browser.find_by_name('submit')
    if submit_button:
        submit_button.click()
        time.sleep(1)  # Wait for the comment to be processed
    else:
        raise Exception("Submit button not found!")

@then('I should see the updated number of comments')
def step_see_updated_comments(context):
    updated_comments_text = context.browser.find_by_css('div.comments h3').text
    print(f"Updated number of comments: {updated_comments_text}")

    execution_time = time.time() - context.start_time
    print(f"Execution Time: {execution_time} seconds")

@then('I close the browser')
def step_close_browser(context):
    context.browser.quit()

