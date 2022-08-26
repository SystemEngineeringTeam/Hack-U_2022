#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import json
import re
import cookpad 
import twi 


df_calorie = pd.read_csv('python/calorie.csv')

# food_number     int64
# food_name      object
# cal             int64

# 日本標準食品成分表をもとにカロリーを計算する
def calc_calorie(ingredients, quantites):
    cal = 0
    for ingredient, quantity in zip(ingredients.values(), quantites.values()):
      print(ingredient, quantity)
      #DBを検索
      searched = df_calorie[df_calorie['food_name'].str.contains(ingredient)]
      #DBに該当する食材があった場合
      if(len(searched.index) > 0):
        print(quantity)
        quantity_int = quantity_convert(quantity)
        print(quantity_int)
        cal += searched. iat[0, 2].item() * quantity_int / 100
    return int(cal)

#　表記揺れのある分量表記を，グラムに変換する
def quantity_convert(quantity):
    # 何g
    if re.match('\d* g', quantity):
      return int(re.sub(r"\D", "", quantity))

    #TODO 1/2を12として計算してしまう
    # 大さじ
    if '大さじ' in quantity:
      return int(re.sub(r"\D", "", quantity))*15
    # 小さじ
    if '小さじ' in quantity:
      return int(re.sub(r"\D", "", quantity))*5

    match quantity:
      case _:
        return 5




def main(food):
# スクレイピングしてjsonに書き込む
    with open('json/recipe.json', 'w') as f:
      f.write('[')
      # food = '豚肉'      #検索したい食材
      # 辞書を要素に持つリストが返る
      # titles, links, images, ingredients_list, quantities_list = cookpad.crawler(food)
      
      #ダミーデータ
      titles = ['簡単♪もやしと豚バラのマヨぽん炒め！', '白菜と豚の煮物', 'グラム100円の豚肉を最高のトンテキに！', '豚肉となす・みょうがの酢醤油炒め', '豚肉の蒲焼き丼', 'モロヘイヤと豚肉のスタミナ炒め', 'キウイでご馳走！柔らか豚ピッツァイオーラ', '簡単にできちゃう！豚肉のピタカ', '豚バラとじゃがいものあまからに', '梅豚', '豚のしょうが焼き']
      links = ['https://cookpad.com/recipe/6296894', 'https://cookpad.com/recipe/7290841', 'https://cookpad.com/recipe/7290797', 'https://cookpad.com/recipe/7290618', 'https://cookpad.com/recipe/7290653', 'https://cookpad.com/recipe/7290397', 'https://cookpad.com/recipe/7279592', 'https://cookpad.com/recipe/7290402', 'https://cookpad.com/recipe/7290250', 'https://cookpad.com/recipe/7290245', 'https://cookpad.com/dining/recipes/2763067']
      images = ['https://img.cpcdn.com/recipes/6296894/894x1461s/1ae484c5209e922e705523a0c1b1cf80?u=23975908&p=1592096864', 'https://img.cpcdn.com/recipes/7290841/894x1461s/e6ee02ccd2cfa4e68400c1f7e19b3241?u=45939868&p=1661083416', 'https://img.cpcdn.com/recipes/7290797/894x1461s/377c51776e72345ec34bbc387923899b?u=5466776&p=1661081383', 'https://img.cpcdn.com/recipes/7290618/894x1461s/af552d2b4cda9fb9fef136babadd0e0a?u=47380115&p=1661080066', 'https://img.cpcdn.com/recipes/7290653/894x1461s/c61d95996b2a73967854080612ae55c7?u=10162422&p=1661074791', 'https://img.cpcdn.com/recipes/7290397/894x1461s/69051384bcc07d65d531a575bc9e16f2?u=7852572&p=1661065260', 'https://img.cpcdn.com/recipes/7279592/894x1461s/7dd70acc6646a0b7216a0333320321fa?u=44510773&p=1660093231', 'https://img.cpcdn.com/recipes/7290402/894x1461s/a3372cf2b5750179c787ba554f5f7014?u=2277874&p=1661063561', 'https://img.cpcdn.com/recipes/7290250/894x1461s/458dbc44fd72c08044a74a0829642385?u=1708736&p=1661055142', 'https://assets.cpcdn.com/assets/blank_logo_recipe_large.png?1b12035e517eeddc39631fb65f35fcad69e4b14bf9275634c54589903d659823', '']
      ingredients_list = [{0: 'もやし', 1: '豚バラ薄切り（切り落とし）', 2: '味付け塩胡椒', 3: 'マヨネーズ', 4: '味ぽん', 5: '小ネギ', 6: 'ミニトマト'}, {0: '白菜', 1: '水', 2: '豚肉', 3: '薄口しょうゆ', 4: '砂糖', 5: 'みりん'}, {0: '豚肉ロース', 1: '塩胡椒', 2: '小麦粉', 3: 'ニンニク', 4: '★ウスターソース', 5: '★醤油', 6: '★みりん', 7: '★砂糖', 8: '★味の素(あれば)', 9: 'バター'}, {0: '豚薄切り肉', 1: 'なす', 2: 'みょうが', 3: '塩コショウ', 4: 'サラダ油', 5: '酢', 6: 'しょうゆ'}, {0: '豚肉', 1: 'ご飯', 2: 'カイワレ', 3: '山葵', 4: '砂糖', 5: '酒', 6: 'みりん', 7: '濃口醤油'}, {0: 'モロヘイヤ', 1: '豚ロース薄切り肉', 2: '玉ねぎ（小）', 3: 'にんにく', 4: 'Aしょうゆ', 5: 'Aみりん', 6: 'A酒', 7: 'サラダ油'}, {0: '豚ロース(トンカツ用)', 1: 'ゼスプリキウイ', 2: '塩', 3: '白ワイン', 4: 'EXバージンオリーブオイル', 5: 'ハーブソルト', 6: 'コショウ', 7: 'ピザ用チーズ', 8: 'バジルの葉、ミニトマト'}, {0: '豚肉', 1: '塩', 2: '小麦粉', 3: 'パルメザンチーズ', 4: '卵', 5: 'オリーブオイル'}, {0: 'じゃがいも', 1: '豚バラ肉', 2: 'ウィンナー', 3: '刻みオクラ', 4: 'ごぼうてん'}, {0: '豚バラブロック', 1: '塩コショウ', 2: 'にんにく', 3: 'しょうが', 4: '長ネギ', 5: '水', 6: '酒', 7: 'しょうゆ', 8: '砂糖', 9: '梅', 10: 'ゆで卵'}, {}]
      quantities_list = [{0: '約100g', 1: '5枚', 2: '適量', 3: '小さじ1/2〜', 4: '小さじ1/2〜', 5: 'あれば、お好みで。', 6: 'あれば、お好みで♪'}, {0: '4/1', 1: '500cc', 2: '適量', 3: '大さじ3', 4: '大さじ3', 5: '大さじ1'}, {0: '１枚又は２枚', 1: '下味程度', 2: '豚肉にまぶす程度', 3: '１片', 4: '大さじ２', 5: '大さじ１', 6: '大さじ１', 7: '砂糖', 8: '３振り', 9: '５g'}, {0: '200g', 1: '3個', 2: '1パック', 3: '少々', 4: '適量', 5: '大さじ1.5', 6: '大さじ1.5'}, {0: '400g程', 1: '適量', 2: '１パック', 3: 'お好み', 4: '大さじ8', 5: '大さじ8', 6: '大さじ8', 7: '大さじ8'}, {0: '1 袋', 1: '200g', 2: '1/2個', 3: '1欠け', 4: '大さじ1', 5: '大さじ1', 6: '大さじ1', 7: '大さじ1'}, {0: '３～４枚(250～300g)', 1: '１個', 2: '小さじ1/3', 3: '大さじ2', 4: '大さじ1', 5: '少々', 6: '少々', 7: '好きなだけ', 8: '適量'}, {0: '500g', 1: '適量', 2: '大さじ3', 3: '少々', 4: '3個', 5: '少々'}, {0: '５個ぐらい', 1: '１パック', 2: '5本', 3: '１袋', 4: '２枚'}, {0: '100g', 1: '少々', 2: '1個', 3: '少々', 4: '1/2本', 5: '200cc', 6: '大3', 7: '大3', 8: '大1', 9: '6個', 10: '2個'}, {}]

      print(titles, links, images, ingredients_list, quantities_list)

      for title, link, image, ingredients, quantities in zip(titles, links, images, ingredients_list, quantities_list):
        #カロリー計算
        cal = calc_calorie(ingredients, quantities)
        #json用に辞書型に変形
        d = {'title':title, 'ingredients':ingredients, 'quantities':quantities, 'calorie':cal, 'image':image, 'link':link}
        #jsonに格納
        json.dump(d, f, indent = 4, ensure_ascii=False)
        
        if titles[-1] != title:
          f.write(',')
      f.write(']')
      f.close()

#twitter
    with open('json/twitter.json', 'w') as f:
      f.write('[')
      texts, links, pictures = twi.printTweetBySearch(food)
      # texts = ['米粉のパンケーキ\n#白崎茶会 さんのレシピよりhttps://t.co/b92RGniIeh\n米粉、甘酒、BP等を使い、梨のコンポートも添えて\n材料の濃縮タイプ甘酒は糀と餅で作った甘酒をブレンダにかけ用意\n\n小麦、卵、乳無しで不安だったけど、きちんと膨らんでくれて安心\n\n#ランチ #おうちごはん #手作りおやつ https://t.co/HIy3qLDpI0', '【ふっくらとした卵そぼろ】\n\nコンビニ弁当などのふっくら甘い卵そぼろを再現！\nかき混ぜ器を使う事で失敗しないレシピになっています♪\n\nhttps://t.co/9GiCOtq0HV\n\n#料理男子\n#料理好きな人と繋がりたい\n#クックパッド\n#クックパッドアンバサダー2022\n#cookpad_news https://t.co/ictCEiMIZU', 'こんにちは🌞\n毎月19日は熟成の日！😌💛\nグランドアルトバイエルンと卵マヨの包み焼きのご紹介です！😉餃子の皮が余ったときに嬉しいアレンジレシピです🥟✨おつまみにぴったりですよ！🍻今日の晩酌のお供にいかがでしょうか？🥰溢れる肉汁がたまらないです～！🥺 https://t.co/gecCIcNSzR', 'みて！この美味しそうなチャプチェとふわふわの卵スープ🤤❤️！\u3000お店のスープみたいやろ？\u3000でもなんとワイ作や✌️✨笑\u3000昨日の晩ごはんは、食事処さくらさん（@mo224co ）のレシピ本で作ってみたの😻✨\u3000ほんのちょっとのコツでこんなに上手なれるなんてハーン感激😭✨めっちゃオススメです😇❤️ https://t.co/8XIJKgQNKR', '今日の1品は…\n\n大葉ツナたまごごはん♪\n\n卵かけごはんのアレンジレシピ♪\n忙しい朝におすすめ😋\n\n＜アメブロ＞\nhttps://t.co/buDXY3WGO6\n\n＜YouTube＞\nhttps://t.co/Q6kCFq2gmP\n\n#料理好きさんと繋がりたい #Twitter料理部 #お腹ぺコリン部 #今日の1品 https://t.co/klNHyN0zRr']
      # links = ['https://t.co/b92RGniIeh', 'https://t.co/9GiCOtq0HV', 'https://t.co/gecCIcNSzR', 'https://t.co/8XIJKgQNKR', 'https://t.co/buDXY3WGO6']
      print(texts)
      print(links)
      print(pictures)
      for text, link, pic in zip(texts, links, pictures):
        d = {'TweetText':text, 'link':link, 'picture':pic}
        json.dump(d, f, indent = 4, ensure_ascii=False)
      f.write(']')
      f.close()


if __name__ == "__main__":
    main('豚')

