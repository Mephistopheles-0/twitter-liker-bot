# Twitter Bot
This Python script is a Twitter bot that automatically likes tweets containing a specific hashtag (#Google in this example). The bot uses the `Tweepy` library to connect to the Twitter API and search for tweets containing the specified hashtag. It then likes each of the tweets found in the search results.

The bot requires authentication with the Twitter API using a set of API keys and access tokens, which can be obtained from the Twitter Developer Portal. These keys and tokens must be included in the script for the bot to function.

The bot also requires the installation of the Tweepy and Pandas libraries, which can be installed using pip and the `requirements.txt` file included with the script.

You can install the requirements by running this command: `pip install -r requirements.txt`, and if you don't have the `.txt` file you can run the command separately like this : `pip install <the package name>`

To use the bot, simply enter the desired hashtag to search for in the script, along with the appropriate API keys and access tokens. The bot can be run from the command line using the python `twitter_bot.py` command. Once running, the bot will automatically like tweets containing the specified hashtag.

Note: Be sure to use the bot responsibly and in compliance with Twitter's Developer Policies and Guidelines.
