import tweepy
import os
import time

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)

#api.update_status("Hello, World! #THWg")
lastUgaId = -1
lastGtId = -1
while(True):
    num = 0
    for tweet in tweepy.Cursor(api.search, q="go dawgs OR godawgs", since_id = lastUgaId, lang="en").items():
        if num == 0:
            lastUgaId = tweet.id
        elif num == 5:
            break
        try:
            api.update_status(status="Go Jackets! #THWg", in_reply_to_status_id=tweet.id)
            sleep(10)
        except tweepy.RateLimitError:
            sleep(900)
        except tweepy.TweepError as e:
            break #for now merely exit out of loop for now
        num += 1
    num = 5
    for tweet in tweepy.Cursor(api.search, q="go jackets OR gojackets", since_id = lastGtId, lang="en").items():
        if num == 5:
            lastGtId = tweet.id
        if num == 10:
            break
        try:
            api.update_status(status="Go Jackets! #TogetherWeSwarm", in_reply_to_status_id=tweet.id)
            sleep(10)
        except tweepy.RateLimitError:
            sleep(900)
        except tweepy.TweepError as e:
            break #for now merely exit out of loop for now
        num += 1
    sleep(300) #sleep for 5 minutes
