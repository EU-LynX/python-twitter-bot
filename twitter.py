import tweepy
import time

auth = tweepy.OAuthHandler('')
auth.set_access_token('')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def main():
    search = ("#lpl")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main()

def main2():
    search = ("#lck")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main2()

def main3():
    search = ("#lec")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main3()

def main4():
    search = ("#lcs")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main4()

def main5():
    search = ("#eslproleague")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main5()

def main6():
    search = ("#valorant")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main6()

def main7():
    search = ("#dota2")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main7()

def main8():
    search = ("#sc2")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main8()

def main9():
    search = ("#esports")
 
    for tweet in tweepy.Cursor(api.search, search, lang='en').items(1):
        try:
            tweet.retweet()
            print("Tweet Retweeted")
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
main9()

while True:
    time.sleep(3600)