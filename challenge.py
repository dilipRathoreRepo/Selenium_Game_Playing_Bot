from selenium import webdriver

selenium_driver_path = "/Users/diliprathore/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=selenium_driver_path)

driver.get("https://www.python.org/")
d = {}

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

for i in range(len(event_times)):
    d[i] = {"time": event_times[i].text, "name": event_names[i].text}

print(d)

driver.quit()
