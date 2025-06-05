from selenium import webdriver

# Set up the Chrome driver
driver = webdriver.Chrome(executable_path='C:\\Users\\afrid\\Desktop\\case2\\chromeDriverWin64\\chromedriver.exe')

# Open a website
driver.get('http://www.google.com')

# Print the title of the page
print(driver.title)

# Close the driver
driver.quit()
