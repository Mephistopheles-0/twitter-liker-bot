import time
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("FZyZgajWPRwqGHfRJObQyeGrj", "Pm1HCabxKfbInR5TeYPnR4GExKwdpjXzJ9ajNoNqN3ODgXa5CO")
auth.set_access_token("1418689975751692293-VV0YvHVW0xUiuspgeKQmcyr0oO6lqF",
                      "0giJUJHuP0aqCWi7sZSNHT17VkoIzlDmqsGO8bI1l1B5L")

# Create API object
api = tweepy.API(auth)

# Define the keyword or hashtag to search for
search_term = "Google"

# Run the loop to like tweets
while True:
    try:
        # Search for tweets containing the keyword or hashtag
        tweets = tweepy.Cursor(api.search_tweets,
                               q=search_term,
                               lang="en").items(10)
        
        # Like the tweets that contain the keyword or hashtag
        for tweet in tweets:
            tweet.favorite()
            print("Liked tweet by @" + tweet.user.screen_name)
            
        # Wait for 15 minutes before running the loop again
        time.sleep(900)

    except tweepy.errors.TweepyException as e:
        print(e.response.text)
        
    except StopIteration:
        break
