# -*- coding: utf-8 -*-
# !/usr/bin/env python
# author = hongkefeng@weidian.com

# download  https://github.com/SavinaRoja/PyUserInput.git
# exec python setup.py install

from selenium import webdriver
from time import sleep
from selenium.webdriver.common import action_chains, keys
from pykeyboard import PyKeyboard

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)
driver.maximize_window()
k = PyKeyboard()


def login(user_name, user_password):
    # 访问主页
    driver.get("https://www.248365365.com/zh-CHS/#/IP/")
    sleep(3)

    # 点击去登录按钮
    driver.find_element_by_xpath('//*[@id="dv1"]/a/div[2]/div[1]').click()
    sleep(5)

    # 点击弹出登录框
    y = driver.find_elements_by_class_name("hm-Login_LoginBtn ")
    y[0].click()
    sleep(3)

    # 输入登录账号
    new_username = driver.find_elements_by_class_name("wl-FailedLogin_Username")[0].send_keys(user_name)
    sleep(3)

    # 点击密码框
    new_password = driver.find_elements_by_class_name("wl-FailedLogin_Password")[0].click()

    action = action_chains.ActionChains(driver)
    action.send_keys(keys.Keys.COMMAND + keys.Keys.ALT + 'i')
    action.perform()
    sleep(3)

    action.send_keys(keys.Keys.ENTER)
    sleep(1)
    k.type_string(user_password)

    new_login = driver.find_elements_by_class_name("wl-FailedLogin_LoginBtn ")
    new_login[0].click()

    sleep(3)

    # 关闭浏览器
    driver.quit()


user_password = "aaaa"
user_name = "bb"

login(user_name, user_password)
