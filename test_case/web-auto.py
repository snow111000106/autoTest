from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        self.driver = webdriver.Chrome(r'/usr/local/bin/chromedriver')

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.ID, "kw").send_keys('测试')
        self.driver.find_element(By.ID, "su").click()