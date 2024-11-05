from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep browser from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# total_articles = driver.find_element(By.XPATH, '//a[@title="Special:Statistics"]').text

#Using ID cSS Selector
total_articles = driver.find_element(By.CSS_SELECTOR, '#articlecount a').text

print(total_articles)


driver.close()