#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from time import sleep


def send_keys(self, text):
    try:
        self.devices.find_element().send_keys(text)
    except Exception as e:
        print(e)
        raise e


def click(self):
    try:
        self.devices.find_element().click()
    except Exception as e:
        print(e)


def get_window_size(self):
    x = self.driver.get_window_size()['width']
    y = self.driver.get_window_size()['height']
    return x, y


def swipe_down(self, t):
    size = self.get_window_size()
    self.driver.swipe(size[0] / 2, size[1] / 4, size[0] / 2, size[1]*3 / 4, t)


def swipe_up(self, t):
    size = self.get_window_size()
    self.driver.swipe(size[0] / 2, size[1] * 3 / 4, size[0] / 2, size[1] / 4, t)


def swipe_left(self, t):
    size = self.get_window_size()
    self.driver.swipe(size[0] / 4, size[1] / 2, size[0] * 3 / 4, size[1] / 2, t)


def swipe_right(self, t):
    size = self.get_window_size()
    self.driver.swipe(size[0] * 3 / 4, size[1] / 2, size[0] / 4, size[1] / 2, t)


def continuity_click(self, element, t):
    for i in (1, t):
        try:
            self.driver.find_element_by_id(element).click()
            sleep(0.1)
        except Exception as e:
            print(e)
        i += 1
