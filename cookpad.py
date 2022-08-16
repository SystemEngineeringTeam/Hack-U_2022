#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




def crawler():
    #読み込み待ち回避
    desired = DesiredCapabilities().CHROME
    desired['pageLoadStrategy'] = 'none'

    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    #ウィンドウサイズの指定
    options.add_argument('--window-size=800,600')
    #画像の非表示
    options.add_argument('--blink-settings=imagesEnabled=false')
    driver = webdriver.Chrome(options=options)
    driver.get('https://cookpad.com')
    # # time.sleep(5)

# 指定したワードで検索する
    search_box = driver.find_element_by_id("keyword")
    search_box.send_keys('もやし')
    search_box.submit()
    # time.sleep(10)

    # for recipe in driver.find_elements_by_class_name('recipe-title'):
    #   recipe.click()
    # TODO:リンクを取得して，一つずつ回るようにする

      #食材と量を出力
      for name in driver.find_elements_by_class_name("name"):
        print(name.text)
      for amount in driver.find_elements_by_class_name("amount"):
        print(amount.text)
      
      driver.back()
      time.sleep(5)

      
    # driver.close()


def main():
    crawler()

if __name__ == "__main__":
    main()