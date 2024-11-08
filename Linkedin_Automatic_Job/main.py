from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#Keep browser from closing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
#Sign_in
driver.get("https://www.linkedin.com/login")
driver.find_element(By.ID, value='username').send_keys('slakshan2862000@gmail.com')
driver.find_element(By.ID, value='password').send_keys('Lamb@123')
driver.find_element(By.XPATH, value="//button[contains(text(),'Sign in')]").click()

driver.get("https://www.linkedin.com/jobs/")
time.sleep(4)
driver.find_element(By.XPATH, value="//input[@aria-label='Search by title, skill, or company'][1]").send_keys('Python Developer', Keys.ENTER)
time.sleep(4)
location = driver.find_element(By.XPATH, value="//input[@aria-label='City, state, or zip code'][1]")
location.clear()
location.send_keys('Bengaluru, Karnataka, India',Keys.ENTER)

driver.find_element(By.XPATH, value="//button[text()='Easy Apply']").click()
time.sleep(7)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

#Save the job application

all_the_jobs = driver.find_elements(By.XPATH, value="//ul[@class='scaffold-layout__list-container']//strong")
# print(all_the_jobs)


for jobs in all_the_jobs:
    jobs.click()
    time.sleep(3)
    driver.find_element(By.XPATH, value="(//span[text()='Save'])[1]").click()
    time.sleep(3)



# #phone no
## Submit the application

# driver.find_element(By.XPATH, value="//label[text()='Mobile phone number']/following-sibling::input").send_keys("8277228629")
# driver.find_element(By.XPATH, value="(//span[text()='Next'])[1]").click()
# driver.find_element(By.XPATH, value="(//span[text()='Next'])[1]").click()
#
# driver.find_element(By.XPATH, value="//span[text()='Submit application']").click()

##HINT: Selenium has a custom exception that gets raised when an element cannot be found it's called NoSuchElementException
