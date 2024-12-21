# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import time
#
# # Set Chrome options
# options = Options()
# options.binary_location = "/usr/bin/chromium"
#
# options = webdriver.ChromeOptions()
#
# # Initialize the Chrome driver service using the correct path
# # Use ChromeDriverManager to automatically download and manage the chromedriver executable
# s = Service(ChromeDriverManager().install())
#
# # Initialize the Chrome driver with the service and options
# browser = webdriver.Chrome(service=s, options=options)
#
# # Open a website
# browser.get("https://codeforces.com/")
# time.sleep(3)
#
# # Find an element by link text and click on it
# link_text = "Enter"
# button = browser.find_element(By.LINK_TEXT, link_text)
# button.click()
# time.sleep(2)
#
# link_text1 = "Gmail"
# button1 = browser.find_element(By.LINK_TEXT, link_text1)
# button1.click()
#
# time.sleep(2)
#
# input_field = browser.find_element(By.XPATH, '//input[@class="whsOnd zHQkBf"]')
# input_field.send_keys("acharyasahil18@gmail.com")
#
# time.sleep(2)
#
# next = browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span')
# next.click()
#
#
# time.sleep(8)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Path to your Chrome WebDriver executable
chrome_driver_path = "/path/to/chromedriver"

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open Google login page
driver.get("https://accounts.google.com")

# Find the email input field and input your email
email_input = driver.find_element_by_xpath("//input[@type='email']")
email_input.send_keys("your_email@gmail.com")

# Click on the Next button
next_button = driver.find_element_by_xpath("//div[@id='identifierNext']")
next_button.click()

# Wait for some time for the password input field to appear
time.sleep(2)

# Find the password input field and input your password
password_input = driver.find_element_by_xpath("//input[@name='password']")
password_input.send_keys("your_password")

# Click on the Next button
next_button = driver.find_element_by_xpath("//div[@id='passwordNext']")
next_button.click()

# You may need to add additional waits and error handling depending on the behavior of the page

# Close the browser
driver.quit()
