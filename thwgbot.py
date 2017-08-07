import tweepy
import os
import time

print(os.environ['CONSUMER_KEY'])
auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)

#api.update_status("Hello, World! #THWg")
lastUgaId = -1
oldUgaId = -1
lastGtId = -1
oldGtId = -1
sleep = False
while True:
    first = True
    for status in tweepy.Cursor(api.search, q="go dawgs OR godawgs", lang ="en").items(5):
        if status.id == oldUgaId:
            break
        if first:
            oldUgaId = lastUgaId
            lastUgaId = status.id
            first = False
        try:
            api.update_status(status="Go Jackets! #THWg", in_reply_to_status_id=status.id)
            sleep(10)
        except tweepy.RateLimitError:
            sleep(900)
        except tweepy.TweepError as e:
            break #for now merely exit out of loop for now
    first = True
    for status in tweepy.Cursor(api.search, q="go jackets OR gojackets", lang="en").items(5):
        if status.id == oldGtId:
            break
        if first:
            oldGtId = lastGtId
            lastGtId = status.id
            first = False
        try:
            api.update_status(status="Go Jackets! #TogetherWeSwarm", in_reply_to_status_id=status.id)
            sleep(10)
        except tweepy.RateLimitError:
            sleep(900)
        except tweepy.TweepError as e:
            break #for now merely exit out of loop for now
        num += 1
    if (sleep):
        sleep(300) #sleep for 5 minutes
        sleep = False
    else:
        sleep = True
