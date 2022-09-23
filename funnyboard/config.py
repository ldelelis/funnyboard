import os


DEBUG = os.getenv("DEBUG", "false").lower() == "true"
TWEETS_ENABLED = os.getenv("TWEETS_ENABLED", "true").lower() == "true"

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
STARBOARD_CHANNEL_ID = os.getenv("STARBOARD_CHANNEL_ID", "")

TWITTER_CONSUMER_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_API_SECRET")

TWITTER_ACCESS_KEY = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
