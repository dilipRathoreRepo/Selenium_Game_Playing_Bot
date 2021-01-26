from selenium import webdriver
from selenium.webdriver.common.keys import Keys

selenium_driver_path = "/Users/diliprathore/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=selenium_driver_path)

URL = "http://secure-retreat-92358.herokuapp.com/"
f_name = "FirstName"
l_name = "LastName"
email = "abc@email.com"

driver.get(URL)
first_name = driver.find_element_by_name("fName")

last_name = driver.find_element_by_name("lName")
email_name = driver.find_element_by_name("email")

first_name.send_keys(f_name)
last_name.send_keys(l_name)
email_name.send_keys(email)

sign_up = driver.find_element_by_class_name("btn-primary")
sign_up.send_keys(Keys.ENTER)
