from selenium import webdriver
from datetime import datetime as dt

selenium_driver_path = "/Users/diliprathore/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=selenium_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

store_item_prices = driver.find_elements_by_css_selector("#store b")
item_details = [price.text for price in store_item_prices]

item_details_dict = {}
for item in item_details:
    if item:
        name = ''.join(item.split('-')[0]).strip()
        price = int(''.join(item.split('-')[1].replace(',', '')).strip())
        item_details_dict[name] = price

print(item_details_dict)


def count_cookies():
    return int(driver.find_element_by_id("money").text)


def buy_item():
    money = count_cookies()
    max_value_item = ""
    for itm, price in item_details_dict.items():
        if money >= price:
            max_value_item = f'{"buy"}{itm}'
            f'money available was {money} and chosen item is {max_value_item}'

    f'Buying item {max_value_item}'
    chosen_item = driver.find_element_by_id(max_value_item)
    chosen_item.click()


now = dt.now()
original_time = now
print(f'time is {now}')

running = True
while running:
    cookie.click()
    new_time = dt.now()
    updated_time = new_time - now
    time_since_original = new_time - original_time
    if time_since_original.total_seconds() > 60:
        running = False
    if updated_time.total_seconds() > 5:
        buy_item()
        now = new_time

driver.quit()
