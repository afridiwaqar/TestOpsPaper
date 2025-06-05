from appium import webdriver

desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformName"] = "Android"
desired_caps["deviceName"] = "Appium_testing_emu"  # Replace with your emulator name

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Find the element by id
element = driver.find_element_by_id("com.example.app:id/button")

# Click the element
element.click()

driver.quit()

