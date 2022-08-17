#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from functools import cache


@cache
def crawler(food):
#読み込み待ち回避
    desired = DesiredCapabilities().CHROME
    desired['pageLoadStrategy'] = 'none'

    options = webdriver.ChromeOptions()
    #画面を表示しない
    options.add_argument('--headless')
    #GPUハードウェアアクセラレーションを無効にする
    options.add_argument('--disable-gpu')
    #ウィンドウサイズの指定
    options.add_argument('--window-size=800,600')
    #画像の非表示
    options.add_argument('--blink-settings=imagesEnabled=false')
    #js無効化
    options.add_experimental_option( "prefs",{"profile.managed_default_content_settings.javascript": 2})
    #日本語
    options.add_argument('--lang=ja')
    driver = webdriver.Chrome(options=options)

    driver.get('https://cookpad.com')
    links = get_link(food,driver)

    ingredients = []
    for link in links:
      driver.get(link)
      ingredients.append(search_ingredients(driver))
      time.sleep(5)
    
    
    #for DEBUG
    # driver.get('https://cookpad.com/recipe/1999481')
    # ingredients = search_ingredients(driver)
    # print(ingredients)

    driver.close()
    return ingredients


# 指定したワードで検索し，リンクを取得
def get_link(food,driver):
    search_box = driver.find_element(by=By.ID, value="keyword")
    search_box.send_keys(food)
    search_box.submit()
    # 各レシピのリンクを取得する
    links = []
    for recipe in driver.find_elements(by=By.CLASS_NAME, value='recipe-title'):
      links.append(recipe.get_attribute("href"))
    
    return links


#食材と量を辞書型で返す
def search_ingredients(driver):
    #print(driver.find_elements(by=By.CLASS_NAME, value="recipe-title"))
    #食材名
    names = driver.find_elements(by=By.CLASS_NAME, value="name")
    #分量
    amounts = driver.find_elements(by=By.CLASS_NAME, value="amount")
    ingredients = {name.text:amount.text for name,amount in zip(names,amounts)}
    
    return ingredients

