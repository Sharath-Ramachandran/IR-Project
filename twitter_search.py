import tweepy
import csv
# Enter the credentials
access_token = "##########################################"
access_token_secret = "########################################"
consumer_key = "##########################################"
consumer_secret = "###########################################"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) # Used to continue until limit
csvFile = open('dataset4.csv', 'w')
csvWriter = csv.writer(csvFile,lineterminator = '\n')

for tweet in tweepy.Cursor(api.search,q="#irony  -filter:retweets",count=100,lang="en",since="2018-11-18").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])


# In this case the query is given as q="#irony". The since parameter can be varied to get tweets from required dates
