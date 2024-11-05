from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep browser from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

#CSS Selector Class
time_of_event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
print(time_of_event)

name_of_event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget a")
print(name_of_event)

#Dictionary
events = {}
for n in range(len(time_of_event)):
    events[n] = {
        "time":time_of_event[n].text,
        "name":name_of_event[n].text,
    }

print(events)

driver.close()