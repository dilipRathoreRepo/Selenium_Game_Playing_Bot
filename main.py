from selenium import webdriver

selenium_driver_path = "/Users/diliprathore/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=selenium_driver_path)

driver.get("https://www.amazon.com.au/Ghost-of-Tsushima-PlayStation-4/dp/B0848TGCRP/ref=sr_1_1?crid=2PGC4LYE1WNGA&dchild=1&keywords=ghost+of+tsushima&qid=1611364462&s=videogames&sprefix=ghost+of%2Caps%2C359&sr=1-1")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)
driver.quit()
