from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://instagram.com")
        sleep(1)
        self.driver.find_element_by_xpath(
            "//input[@name='username']").send_keys(username, Keys.TAB, password, Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "//button[contains(text(), 'Not Now')]").click()
        self.driver.find_element_by_xpath(
            f"//a[contains(@href, '/{username}')]").click()
        sleep(1)

    def get_not_following_back(self):
        # Check following
        self.driver.find_element_by_xpath(
            f"//a[contains(@href, '/following')]").click()
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]")
        last_ht = 0
        ht = 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                               return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name("a")
        following = [name.text for name in links if name.text != ""]
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()

        # Check followers
        self.driver.find_element_by_xpath(
            f"//a[contains(@href, '/followers')]").click()
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[2]")
        last_ht = 0
        ht = 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                               return arguments[0].scrollHeight;""", scroll_box)
        links = scroll_box.find_elements_by_tag_name("a")
        followers = [name.text for name in links if name.text != ""]
        self.driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div[1]/div/div[2]/button").click()

        #################
        self.not_following_back = [
            name for name in following if name not in followers]

        # Write all the people not following you back in a file
        # with open("Not_Following_Back", "w") as file:
        #     for name in self.not_following_back:
        #         file.write(name + "\n")
