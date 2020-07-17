from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class Instabot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        sleep(1)
        self.driver.find_element_by_xpath(
            "//input[@name='username']").send_keys(username, Keys.TAB, password, Keys.ENTER)
        sleep(3)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_xpath(
            f"//a[contains(@href=/{username}/)]")
