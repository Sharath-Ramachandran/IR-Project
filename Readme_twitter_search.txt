The python library tweepy should be installed to run the program. User credentials has to be entered instead of the ## values. The program will display the tweets in the prompt and continue until the limit is reached. The tweets will be written into a csv file with the tweet text and timestamp. 
The query parameter q in the for loop can be modified to get different datasets. 
For getting tweets with the word irony, q="irony  -filter:retweets"
For getting tweets with the hashtags #irony, #sarcasm , q="#irony OR #sarcasm  -filter:retweets"
The 'since' parameter can be varied to get tweets from different dates.