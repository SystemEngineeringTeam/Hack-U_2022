#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import re
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
        print(amount)
        amount_int = amount_convert(amount)
        print(amount_int)
        cal += searched. iat[0,2].item() * amount_int / 100
        # print(cal)
      
      # print(name)
      # print(searched)
      # print(cal)
    return cal


def amount_convert(amount):
    # 何g
    if re.match('\d* g',amount):
      return int(re.sub(r"\D", "", amount))

    # 大さじ
    if '大さじ' in amount:
      return int(re.sub(r"\D", "", amount))*15
    # 小さじ
    if '小さじ' in amount:
      return int(re.sub(r"\D", "", amount))*5
    
    match amount:
      case _:
        return 5



def main():
# スクレイピングしてjsonに書き込む
    with open('recipe.json','w') as f:
      food = '豚肉'
      #辞書を要素に持つリストが返る
      # titles,links,ingredients_list = cookpad.crawler(food)
      titles = ['豚肉の\u3000みそ焼き', 'レシピ投稿祭 大葉チーズin豚巻ピーマン', '簡単\u3000我が家の丼✨豚のハニーマスタード丼', '大葉とチーズの豚肉巻き☆ソース2種', '我が家の丼 スタミナとろろ豚丼', 'ビールにピッタリ\u3000豚バラ炒め', 'ねぎ塩豚バラ', '茄子と豚バラのピリ辛胡麻油炒めです', 'ピーマンと豚肉のピリ辛炒め', '豚肉とナスの重ね蒸し（にんにく味噌ダレ）', '豚のしょうが焼き']
      links = ['https://cookpad.com/recipe/7285885', 'https://cookpad.com/recipe/7285907', 'https://cookpad.com/recipe/7285786', 'https://cookpad.com/recipe/7285880', 'https://cookpad.com/recipe/7285843', 'https://cookpad.com/recipe/7285821', 'https://cookpad.com/recipe/7267910', 'https://cookpad.com/recipe/7285749', 'https://cookpad.com/recipe/7285615', 'https://cookpad.com/recipe/7278411', 'https://cookpad.com/dining/recipes/2763067']
      ingredients_list = [{'豚肉\u3000やわらかいもの': '200g', '赤みそ': '30gくらい', '砂糖': '大さじ3', '酒': '少量', 'みりん': '少量', 'いりごま白': '少量', '★ガーゼ': '味噌の味を お肉にしみらせるために使う'}, {'ピーマン': '4個', 'ピザ用チーズ': '80g', '大葉': '8枚', '豚バラ肉': '8枚', '塩コショウ': '適宜', '小麦粉': '適宜', '油': '適宜'}, {'豚肉（ローステキカツ用）': '300g', 'オリーブ油': '大さじ1', '塩コショウ': '適量', 'ブラックペッパー': '適量', 'キャベツ': '適量（好きなだけ）', '大葉': '10枚程', 'トマト': '2個', 'ポン酢': '適量', '☆粒マスタード': '大さじ3', '☆マヨネーズ': '大さじ1', '☆ハチミツ': '小さじ1', 'レモスコ（あれば）': '適量'}, {'豚バラ肉': '8枚', '大葉': '4枚', 'さけるチーズ': '2本', '☆梅干し（大）': '1個', '☆ポン酢': '大さじ1.5', '◎醤油': '大さじ1', '◎酒': '大さじ1', '◎みりん': '大さじ1', '◎砂糖': '大さじ1'}, {'味噌': '大さじ3', 'ヨーグルト': '大さじ1', 'アスパラ': '4本', 'トマト': '2個', 'とろろ': '1/3', '卵': '2個', '塩': '少し', '水': 'お鍋いっぱい', '豚肉': '4枚', 'ご飯': 'お茶碗4杯', 'マヨネーズ': '少し', '豆苗': '少し'}, {'豚バラ肉': '好きなだけ', 'ごま\u3000最後にふりかけ用': '適量', 'にんにく\u3000チューブ': '多めに', 'しょうゆ': '少し', 'コチュジャン': '主役なので多めに', '砂糖': 'ニンニクくらいは', 'ごま油': '適量', '唐辛子\u3000一味でも可': '好きなだけ'}, {'豚バラ薄切り肉': '150g', '長ネギ': '半分', '(A)鶏ガラスープの素': '小さじ1', '(A)すりおろしニンニク': '小さじ1/2', '(A)お酢': '小さじ1/2', '(A)砂糖': 'ふたつまみ', '(A)塩': 'ふたつまみ', '(A)みりん': '小さじ1', '(A)水': '大さじ1', '(A)ごま油': '大さじ2', '(A)粗びき黒こしょう': '適量'}, {'青葱': '適量', '豚バラ肉': '１００g', '茄子': '１本', '合わせ調味料': '＊＊＊', '胡麻油': '５０㍉', 'めんつゆ': '１０㍉', '胡麻': '大１', '七味': '少々', '豆板醤': '大１'}, {'ピーマン': '5個', '豚肉（薄切りのもの）': '200g前後', '胡麻油': '大さじ1程度', '酒': '大さじ1', '砂糖': '小さじ1', '醤油': '大さじ1', '豆板醤': '小さじ1/2'}, {'ナス（輪切り）': '2本', '豚肉（バラかロース・しゃぶしゃぶ用）': '２００g', '料理酒（蒸し用）': '大さじ1', '★白ねぎ（みじん切り）': '１／２本', '★ニンニク（チューブ）': '4㎝程度', '★味噌': '大さじ１', '★料理酒': '大さじ２', '★みりん': '大さじ１', '★砂糖': '大さじ１', '★しょうゆ': '大さじ1', '★いりごま（白）※すりごまでもOK': '大さじ１', '★水\u3000※味が濃い時や固さの調整に使用': '小さじ１程度'}, {}]

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