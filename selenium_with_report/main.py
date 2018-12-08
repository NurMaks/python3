from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:


    def __init__(self, username, password):
        self.username = username
        self.password =password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())


    def closeBrowser(self):
        self.driver.close()


    def signin(self):
        # "//a[@href='/accounts/login/?source=auth_switcher']"
        #(username='ainur_sabit_', password='test123')
        # "//input[@name='username']"
        # "//input[@name='password']"
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)

        signin_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']")
        signin_button.click()
        time.sleep(2)

        username_input = driver.find_element_by_xpath("//input[@name='username']")
        password_input = driver.find_element_by_xpath("//input[@name='password']")

        username_input.clear()
        password_input.clear()

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)



    def like_photo(self, hashtag):
        # "//span[@aria-label='Нравится']"
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range(0, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        #getting picture links
        links = driver.find_elements_by_tag_name('a')
        links_url = [url.get_attribute('href') for url in links]

        print('LENGTH', str(len(links_url)) )
        for img_url in links_url:
            driver.get(img_url)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                driver.find_element_by_xpath("//span[@aria-label='Like']").click()
                time.sleep(2)
            except Exception as ex:
                time.sleep(2)


username = input('username: ')
password = input('password: ')
while True:
    hashtag = input("hashtag to LIKE: ")
    bot = InstagramBot(username=username, password=password)
    bot.signin()
    bot.like_photo(hashtag)