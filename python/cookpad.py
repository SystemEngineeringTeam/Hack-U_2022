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
    options.add_argument('--headless')
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

#https://cookpad.comにアクセス，検索
    driver.get('https://cookpad.com')
    titles, links = get_link(food, driver)

# 検索結果から取得したレシピページにアクセス
    ingredients_list = [] #　材料
    quantities_list = [] #　分量
    images = [] # レシピ画像
    for link in links:
      driver.get(link)

      # CookpadDining(有料コンテンツ)は画像，レシピが取得できない．
      try:
        mainphoto = driver.find_element(by=By.XPATH, value='//*[@id="main-photo"]/img')
        image = mainphoto.get_attribute('src')
        images.append(image)
      except :
        print('画像を取得できませんでした')
        images.append('')

      ingredients, amounts = search_ingredients(driver)
      ingredients_list.append(ingredients)
      quantities_list.append(amounts)
      # 負荷軽減のため
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
    #食材名を取得
    names = driver.find_elements(by=By.CLASS_NAME, value="name")
    #分量を取得
    amounts = driver.find_elements(by=By.CLASS_NAME, value="amount")
    #取得した食材と分量をindexと共にそれぞれdictに追加する
    for i, name, amount in zip(range(len(names)), names, amounts):
      ingredients.update({i+1:name.text})
      quantities.update({i+1:amount.text})
    
    return ingredients, quantities

# def main():
#   crawler('もやし')

# if __name__ == "__main__":
#     main()