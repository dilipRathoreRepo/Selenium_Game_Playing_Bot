from selenium import webdriver

selenium_driver_path = "/Users/diliprathore/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=selenium_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element_by_css_selector("#articlecount a")
print(article_count.text)

search = driver.find_element_by_name("search")
search.send_keys("Python")

from selenium.webdriver.common.keys import Keys
search.send_keys(Keys.ENTER)

driver.quit()
