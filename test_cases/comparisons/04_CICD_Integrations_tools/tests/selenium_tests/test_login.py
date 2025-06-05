from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/auth/login")
    driver.find_element_by_name("email").send_keys("admin@helloflask.com")
    driver.find_element_by_name("password").send_keys("helloflask")
    driver.find_element_by_name("submit").click()
    assert "Home - Albumy" in driver.title
    driver.quit()
