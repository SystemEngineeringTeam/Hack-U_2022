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
    # 100件　* 10回取得 = 1000件
    # for i in range(3):
    tweets = client.search_recent_tweets(
        query=s,  # 検索ワード
        max_results=100,  # 取得件数
        tweet_fields = ['entities','public_metrics'],
    )

    texts = []
    links = []
    # print(tweets)                  # ツイート内容
    for tweet in tweets.data:
        #いいねが5以上
        if tweet.public_metrics["like_count"] > 5:
            print("--------------------")
            print(tweet.id)
            print(tweet.public_metrics["like_count"])
            print(tweet.text)
            texts.append(tweet.text)
            urls = tweet.entities['urls']
            urls = urls[0]
            links.append(urls['url'])

    return texts,links


def main():
    texts,links = printTweetBySearch('豚肉　レシピ')
    print(texts,links)

if __name__ == "__main__":
    main()
