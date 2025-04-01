import tweepy
import json

# Twitter API Credentials (replace with your own keys)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

# Authenticate
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Collect Tweets
query = "AI OR LLM OR MachineLearning -filter:retweets"
tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", tweet_mode="extended").items(500)

# Store in a JSON file
with open("tweets.json", "w") as f:
    json.dump([tweet._json for tweet in tweets], f, indent=4)

print("Data collection complete!")
