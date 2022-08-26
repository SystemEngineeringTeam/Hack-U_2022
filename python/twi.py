import os
from os.path import join, dirname
from dotenv import load_dotenv
import tweepy
from datetime import datetime,timedelta



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

    now = datetime.now()
    now = now.replace(minute=0, second=0, microsecond=0)
    end_time_tweepy = str(now.isoformat())+'+09:00'
    start_time = now - timedelta(days=6) 
    start_time_tweepy = str(start_time.isoformat())+'+09:00'

    texts = []
    links = []
    pictures = []
    for tweet in tweepy.Paginator(client.search_recent_tweets, 
                            query=s+'レシピ has:images', start_time=start_time_tweepy, end_time=end_time_tweepy,
                            tweet_fields=['entities','public_metrics'], 
                            max_results=100).flatten(limit=1000):
        # print(tweet)
        #いいねが5以上
        if tweet.public_metrics["like_count"] > 5:
            
                print("--------------------")
                print(tweet.id)
                # print(tweet.public_metrics["like_count"])
                # print(tweet.text)
                texts.append(tweet.text)

                #リンク
                urls = tweet.entities['urls']
                urls = urls[0]
                links.append(urls['url'])

                #画像
                pics = urls['images']
                pics = pics[0]
                pictures.append(pics['url'])

            

    return texts,links,pictures


def main():
    texts,links,pictures = printTweetBySearch('豚')
    print(texts,links,pictures)

if __name__ == "__main__":
    main()
