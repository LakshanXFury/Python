from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Keep browser from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

driver.find_element(By.NAME,'fName').send_keys('Lakshan')
driver.find_element(By.NAME,'lName').send_keys('S')
driver.find_element(By.NAME,'email').send_keys('lakshan@gmail.com')

driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()


#
# driver.close()


