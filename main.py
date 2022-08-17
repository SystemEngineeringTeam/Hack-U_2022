#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import route, run, template, redirect, request
import pandas as pd
import numpy as np
import dask.dataframe as dd
import json
import cookpad
import twi


df_calorie = pd.read_csv('calorie.csv')
# food_number     int64
# food_name      object
# cal             int64


def calc_calorie(ingredients):
    cal=0
    for name,amount in ingredients.items():
      searched =  df_calorie[df_calorie['food_name'].str.contains(name)]

      #DBに該当データがあった場合
      if(len(searched.index) > 0):
        cal += searched.iat[0,2].item()
        # print(cal)
      
      # print(name)
      # print(searched)
      # print(cal)
    return cal


def main():
    with open('recipe.json','w') as f:
      food = 'もやし'
      #辞書を要素に持つリストが返る
      titles,links,ingredients_list = cookpad.crawler(food)
      # ingredients_list=[{'もやし': '一袋', 'ごま油': '適量', '酢': '適量', '鶏ガラスープ 顆粒': 'ひとふり', '唐辛子 輪切り': '適量', 'にんにく チューブ': '少し', '塩': 'しおしお', '炒りごま': '好きなだけ'}, {'もやし': '100g', '豆苗': '200g', 'ツナ（オイル入り）': '1缶', '豆板醤': '適宜', 'ごま油': '大さじ1', '塩コショウ': '適宜', '醤油': '適宜'}, {'キャベツ': '適量', 'もやし': '1/2袋', '卵': '1個', '卵の水': '大さじ1/2', '水': '1200cc〜', 'だし': '適量', '味噌': '適量'}, {'もやし': '1袋', 'きゅうり': '1本', 'キムチ': '好きなだけ', '鶏がらの素': '小さじ1ちょい', 'ごま油': '小さじ1', 'ラー油': '小さじ2分の1'}, {'もやし': '1袋', '塩': 'ひとつまみ', 'ごま油': '少々', 'キムチ鍋の素': '大さじ1〜2', 'ごま': 'お好みの量'}, {'豚肉': '小分けのブロック1個', '葱': '3本', 'もやし': '1袋', '餡': 'お好み', '水': 'お好み調整'}, {'もやし': '１袋', 'ズッキーニ': '1/2本', 'だし醤油': '小さじ１', '塩昆布': '３g'}, {'もやし': '1袋', 'レタス': '1/2個', '卵': '2個', 'オイスターソース': '大さじ1杯', 'しょうゆ': '大さじ1杯', 'サラダ油': '適量'}, {'濃口醤油': '大さじ3.5', 'みりん': '小さじ2', 'ごま油': '小さじ2', '鶏がらスープのもと': '小さじ2', '味の素': '小さじ1', 'ほんだし': '小さじ1/2', '水': '1000cc', 'ラード（チューブ）': 'お好みで', 'もやし': '2袋', '青ねぎ': '適量', 'ブラックペッパー': '適量'}, {'豆もやし': '1袋', '長ネギ': '1本', '塩、胡椒': '適量', 'しょうゆ': '少々', 'ゴマ油': '適量', '一味唐辛子': '好みで', 'すりごま': '適量', 'にんにく': '1かけ'}, {}]

      for title,link,ingredients in zip(titles,links,ingredients_list):
        cal = calc_calorie(ingredients)
        d = {'title':title, 'calorie':cal, 'link':link}
        json.dump(d,f,indent = 4, ensure_ascii=False)


if __name__ == "__main__":
    main()
# @route('/hello')
# def hello():
#     return "Hello World!"

# run(host='localhost', port=8080, debug=True)