#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
from appium import webdriver


def initial_devices(desired_caps=None):
    """初始化移动端"""

    global devices
    desired_caps = {}
    command_executor = "http://localhost:4723/wd/hub"

    desired_caps['platformName'] = 'Android'  # 设备系统
    desired_caps['platformVersion'] = '6.0'  # 设备系统版本
    desired_caps['deviceName'] = 'LZKNWCLZUOJZ5HPF'  # 设备名称
    # desired_caps['app'] = os.path.abspath('/Users/snow/Downloads/app-huawei-release_6434.apk')
    desired_caps['appPackage'] = 'com.xingjiabi.shengsheng'
    desired_caps['appActivity'] = 'com.xingjiabi.shengsheng.app.SplashActivity'
    # desired_caps['appWaitActivity'] ='com.xingjiabi.shengsheng.mine.XjbLoginActivity'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['noReset'] = True
    devices = webdriver.Remote(command_executor, desired_caps)

    return devices


def release_devices():
    devices.quit()


if __name__ == '__main__':
    initial_devices()