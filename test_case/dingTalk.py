#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os, sys,csv
from time import sleep
import unittest
from selenium import webdriver
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class Mytest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 设备系统
        desired_caps['platformVersion'] = '6.0'  # 设备系统版本
        desired_caps['deviceName'] = 'LZKNWCLZUOJZ5HPF'  # 设备名称
        desired_caps['appPackage'] = 'com.alibaba.android.rimet'
        desired_caps['appActivity'] = '.biz.SplashActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动app

    def get_window_size(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_down(self, t):
        size = self.get_window_size()
        self.driver.swipe(size[0] / 2, size[1] / 4, size[0] / 2, size[1]*3 / 4, t)

    def test_case(self):
        sleep(2)
        self.driver.find_elements_by_id('com.alibaba.android.rimet:id/home_action_bar_button_icon')[1].click()
        sleep(2)
        self.driver.find_element_by_id('android:id/search_src_text').send_keys('直播小组密室')
        sleep(1)
        self.driver.find_element_by_id('com.alibaba.android.rimet:id/ll_text').click()
        sleep(2)
        contexts = []
        for n in range(0, 3):
            for i in range(0, 10):
                try:
                    contexts.append(self.driver.find_elements_by_id('com.alibaba.android.rimet:id/chatting_content_tv')[i].text)
                except IndexError:
                    pass
            self.swipe_down(1000)
            sleep(3)
        print(set(contexts))
        self.driver.find_element_by_id('com.alibaba.android.rimet:id/img_back').click()
        sleep(2)
        self.driver.find_element_by_id('android:id/up').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
