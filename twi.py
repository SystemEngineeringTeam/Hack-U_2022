import os
from os.path import join, dirname
from dotenv import load_dotenv

import tweepy



##################################################################
## トークン関連
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


CK  =  os.environ.get("CK")
CS  =  os.environ.get("CS")
AT  =  os.environ.get("AT")
ATS =  os.environ.get("ATS")
BT =  os.environ.get("BT")

##################################################################


client = tweepy.Client(
    consumer_key=CK,
    consumer_secret=CS,
    access_token=AT,
    access_token_secret=ATS,
    bearer_token=BT
)

def printTweetBySearch(s):
    tweets = client.search_recent_tweets(
        query='レシピ',  # 検索ワード
        max_results=20  # 取得件数
    )

    print(tweets)                  # ツイート内容
    
def main():
    printTweetBySearch('レシピ')

if __name__ == "__main__":
    main()
