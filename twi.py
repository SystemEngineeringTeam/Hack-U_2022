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
        query='レシピ 卵',  # 検索ワード
        max_results=100,  # 取得件数
        tweet_fields = ['public_metrics']
    )

    # print(tweets)                  # ツイート内容
    for tweet in tweets.data:
        if tweet.public_metrics["like_count"] > 5:
            print("--------------------")
            print(tweet.id)
            print(tweet.public_metrics["like_count"])
            print(tweet.text)

def main():
    printTweetBySearch('レシピ')

if __name__ == "__main__":
    main()
