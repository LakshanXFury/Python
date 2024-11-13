from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests


#Keep browser from closing

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
web_page = response.text

soup = BeautifulSoup(web_page,"html.parser")

link_to_property = (soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor"))
# print(link_to_property)

address = (soup.find_all(name="address"))
# print(address)

price = (soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine"))
# print(price)


for link, addresses, prices in zip(link_to_property, address, price):
    property_link = link.get("href")
    property_address = addresses.getText().strip()
    property_prices = prices.getText()

    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdt3Nygof_Jlu4aVSPe97VjJZ7VkoHj5QObEDYnTiJ4XAfILg/viewform")
    time.sleep(4)
    #address
    address_input = driver.find_element(By.XPATH, value="//span[text()='What is the address of the property']"
                                                        "//ancestor::div[3]/following-sibling::div//input")
    address_input.send_keys(property_address)
    #Price
    price_input = driver.find_element(By.XPATH, value="//span[text()='What is the price per month ?']"
                                                      "//ancestor::div[3]/following-sibling::div//input")
    price_input.send_keys(property_prices)
    #Link
    link_input = driver.find_element(By.XPATH, value="//span[text()='What is the link to the property ?']"
                                                     "//ancestor::div[3]/following-sibling::div//input")
    link_input.send_keys(property_link)

    try:
        driver.find_element(By.XPATH, value="//span[text()='Submit']").click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, value="//span[text()='Senden']").click()
    finally:
        time.sleep(2)
driver.close()