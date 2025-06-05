import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

@given('I open the login page')
def step_open_login_page(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    context.driver.get("http://127.0.0.1:5000/auth/login")

@when('I fill in the login form with valid credentials')
def step_fill_login_form(context):
    context.driver.find_element(By.ID, 'email').send_keys('admin@helloflask.com')
    context.driver.find_element(By.ID, 'password').send_keys('helloflask')

@when('I submit the login form')
def step_submit_login_form(context):
    context.driver.find_element(By.ID, 'submit').click()

@then('I should be logged in')
def step_verify_login(context):
    WebDriverWait(context.driver, 10).until(EC.invisibility_of_element((By.ID, 'email')))

@when('I navigate to the upload page')
def step_navigate_to_upload_page(context):
    context.driver.get("http://127.0.0.1:5000/upload")

def step_upload_images(context, num_images):
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]')))
    
    image_paths = [f'/media/waqar/databackups/Downloads/papers/Image_{i}.jpg' for i in range(1, num_images + 1)]
    
    for path in image_paths:
        try:
            file_input = WebDriverWait(context.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="file"]'))
            )
            file_input.send_keys(path)
            print(f"Uploaded {path}")  # Debugging line
            
            context.driver.execute_script("document.querySelector('form').reset();")
            time.sleep(1)
        except TimeoutException:
            print(f"Failed to upload {path}: Timeout waiting for file input element")
        except Exception as e:
            print(f"Failed to upload {path}: {e}")
    
    try:
        submit_button = WebDriverWait(context.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-light.float-right'))
        )
        submit_button.click()
    except TimeoutException:
        print("Failed to click the submit button: Timeout waiting for button")
    except Exception as e:
        print(f"Failed to click the submit button: {e}")

@when('I upload 1 image')
def step_upload_single_image(context):
    step_upload_images(context, 1)

@when('I upload another 1 image')
def step_upload_another_image(context):
    step_upload_images(context, 1)
    
@then('I should see a success message')
def step_verify_upload(context):
    time.sleep(5)  # Adjust the timeout as needed
    success_message = context.driver.find_element(By.CSS_SELECTOR, '.success-message-selector')  # Replace with actual selector
    assert success_message.is_displayed()

def after_all(context):
    context.driver.quit()

