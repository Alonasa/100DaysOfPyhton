from selenium import webdriver
from selenium.webdriver.common.by import By

PRODUCT_LINK = "https://www.python.org/events/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(PRODUCT_LINK)
full_data = driver.find_elements(By.CLASS_NAME, "list-recent-events li")
events = {}
for i, val in enumerate(full_data):
    title = val.find_element(By.CLASS_NAME, "event-title").text
    date = val.find_element(By.TAG_NAME, "time")
    short_date = date.text
    full_date = date.get_attribute("datetime")
    location = val.find_element(By.CLASS_NAME, "event-location")

    events[i] = {
        'title': title,
        'date': date.text,
        'short date': short_date,
        'full date': full_date,
        'location': location.text,
    }

print(str(events).encode('utf-8'))

driver.quit()
