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
        time.sleep(4)
        try:
            self.driver.find_element(By.XPATH, value="//button[text()='I Accept']").click()
            time.sleep(4)
        except NoSuchElementException:
            self.driver.find_element(By.XPATH, value="//button[text()='Continue']").click()
        finally:
            time.sleep(5)
            go_button = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
            go_button.click()

        time.sleep(60)
        self.download_speed = float(self.driver.find_element(By.XPATH, value="//div[text()[normalize-space()='Download']]"
                                                                   "/following-sibling::div/span").text)
        print(self.download_speed)

    def tweet_at_provider(self):
         if self.download_speed < 100:
            self.driver.get("https://twitter.com/login")
            time.sleep(7)
            self.driver.find_element(By.XPATH, '//input[@autocomplete="username"]').send_keys(TWITTER_EMAIL)
            self.driver.find_element(By.XPATH, value="//span[text()='Next']").click()
            time.sleep(4)

            try:
                # Try to find an element
                self.driver.find_element(By.XPATH, value='//input[@autocomplete="current-password"]').send_keys(TWITTER_PASSWORD)
                time.sleep(2)
                self.driver.find_element(By.XPATH, value="//span[text()='Log in']").click()

            except NoSuchElementException:
                # Handle the case when the element is not found
                self.driver.find_element(By.XPATH, value="//span[text()='Phone or username']//ancestor::div[2]/following-sibling::div//"
                                                    "input").send_keys(TWITTER_USERNAME)
                self.driver.find_element(By.XPATH, value="//span[text()='Next']").click()
                time.sleep(4)
                self.driver.find_element(By.NAME, value="password").send_keys(TWITTER_PASSWORD)
                self.driver.find_element(By.XPATH, value="//span[text()='Log in']").click()

            finally:
                time.sleep(4)
                post = self.driver.find_element(By.XPATH, value="(//div[text()='What is happening?!']/parent::div/following-sibling::div//div)[4]")
                post.send_keys(f"Hi @BSNLCorporate \n Why is my internet speed {self.download_speed}mbps down, when I pay for 100 mbps down")
                time.sleep(4)
                self.driver.find_element(By.XPATH, value="//span[text()='Post']").click()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
