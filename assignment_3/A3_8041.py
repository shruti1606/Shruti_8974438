from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Element_1: Go to the Job Bank Canada website
driver.get('https://www.jobbank.gc.ca/home')
time.sleep(5)

# Element_2: Find sign in/registration button
registration_button = driver.find_element("xpath","/html/body/header/div[2]/div/div/nav/form/ul/li/button")
registration_button.click()
time.sleep(5)

# Element_3: find the job seeker tab and click it
jobseeker_button = driver.find_element("xpath","/html/body/header/div[2]/div/div/nav/form/ul/li/ul/li[1]/a")
jobseeker_button.click()
time.sleep(5)

# Element_4: Find the email input field and enter the email address
email_input = driver.find_element("id","loginForm:input-email")
email_input.send_keys("xiap1606@gmail.com")
time.sleep(3)

# Element_5: Find the continue button and click it
continue_button = driver.find_element("id","loginForm:loginProcess")
continue_button.click()
time.sleep(5)

# Element_6: Find the password input field and enter the password
password_input = driver.find_element("id","loginForm:input-password")
password_input.send_keys("Xiajobbank@1606")
time.sleep(5)

# Element_7: Find the signin button and click it
signin_button = driver.find_element("id","loginStandardPlusUser")
signin_button.click()
time.sleep(5)

# Element_8: Security question
sequrity1_button = driver.find_element("id","securityForm:input-security-answer")
sequrity1_button.send_keys()
time.sleep(15)

# Element_9: Find the countinue button and click it
countinue_button = driver.find_element("xpath","/html/body/main/div[2]/form/fieldset/div/div[2]/button[1]")
countinue_button.click()
time.sleep(5)

# Close the browser
driver.quit()