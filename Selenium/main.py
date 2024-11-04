from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep browser from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.implicitly_wait(20)

whole_price = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
fraction_price = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price is {whole_price}.{fraction_price}")




# driver.close() #Closes the one tab
driver.quit() #Quits the entire browser

