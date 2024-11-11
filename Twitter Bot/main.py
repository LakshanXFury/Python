from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWNLOAD = 100
TWITTER_EMAIL = "slakshan2862000@gmail.com"
TWITTER_PASSWORD = "Lamb@123"
TWITTER_USERNAME = "@fury_auraa"


#Keep browser from closing

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.maximize_window()

#Sign_in

# driver.get("https://twitter.com/login")
# time.sleep(7)
# driver.find_element(By.XPATH, '//input[@autocomplete="username"]').send_keys(TWITTER_EMAIL)
# driver.find_element(By.XPATH, value="//span[text()='Next']").click()
# time.sleep(4)
#
# try:
#     # Try to find an element
#     driver.find_element(By.XPATH, value='//input[@autocomplete="current-password"]').send_keys(TWITTER_PASSWORD)
#     time.sleep(2)
#     driver.find_element(By.XPATH, value="//span[text()='Log in']").click()
#
# except NoSuchElementException:
#     # Handle the case when the element is not found
#     driver.find_element(By.XPATH, value="//span[text()='Phone or username']//ancestor::div[2]/following-sibling::div//"
#                                         "input").send_keys(TWITTER_USERNAME)
#     driver.find_element(By.XPATH, value="//span[text()='Next']").click()
#     time.sleep(4)
#     driver.find_element(By.NAME, value="password").send_keys(TWITTER_PASSWORD)
#     driver.find_element(By.XPATH, value="//span[text()='Log in']").click()


# finally:
#     driver.close()


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.XPATH, value="//span[text()='Go']").click()


    def tweet_at_provider(self):
        pass

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
