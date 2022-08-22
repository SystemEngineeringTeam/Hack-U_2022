#!/usr/bin/env python
# -*- coding: utf-8 -*-
from statistics import quantiles
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
    # options.add_argument('--headless')
    #GPUハードウェアアクセラレーションを無効にする
    options.add_argument('--disable-gpu')
    #ウィンドウサイズの指定
    options.add_argument('--window-size=800, 600')
    #画像の非表示
    options.add_argument('--blink-settings=imagesEnabled=false')
    #js無効化
    options.add_experimental_option( "prefs", {"profile.managed_default_content_settings.javascript": 2})
    #日本語
    options.add_argument('--lang=ja')
    driver = webdriver.Chrome(options=options)

    driver.get('https://cookpad.com')
    titles, links = get_link(food, driver)

    ingredients_list = []
    quantities_list = []
    images = []
    for link in links:
      
      driver.get(link)

      try:
        mainphoto = driver.find_element(by=By.XPATH, value='//*[@id="main-photo"]/img')
        image = mainphoto.get_attribute('src')
        print(image)
        images.append(image)
      except :
        print('画像を取得できませんでした')
        images.append('')

      ingredients, amounts = search_ingredients(driver)
      ingredients_list.append(ingredients)
      quantities_list.append(amounts)
      time.sleep(1)
    
    # print(ingredients)
    #for DEBUG
    # driver.get('https://cookpad.com/recipe/1999481')
    # ingredients = search_ingredients(driver)

    driver.close()
    return titles, links, images, ingredients_list, quantities_list


# 指定したワードで検索し，リンクを取得
def get_link(food, driver):
    search_box = driver.find_element(by=By.ID, value="keyword")
    search_box.send_keys(food)
    search_box.submit()
    # 各レシピのリンクを取得する
    titles = []
    links = []
    for recipe in driver.find_elements(by=By.CLASS_NAME, value='recipe-title'):
      titles.append(recipe.text)
      links.append(recipe.get_attribute("href"))
    
    return titles, links


#食材と量を辞書型で返す
def search_ingredients(driver):
    ingredients = {}
    quantities = {}
    #print(driver.find_elements(by=By.CLASS_NAME, value="recipe-title"))
    #食材名
    names = driver.find_elements(by=By.CLASS_NAME, value="name")
    #分量
    amounts = driver.find_elements(by=By.CLASS_NAME, value="amount")
    for i, name, amount in zip(range(len(names)), names, amounts):
      ingredients.update({i:name.text})
      quantities.update({i:amount.text})
    
    return ingredients, quantities

# def main():
#   crawler('もやし')

# if __name__ == "__main__":
#     main()