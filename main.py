import discord

from funnyboard.config import DISCORD_TOKEN, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET, TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET
from funnyboard.dps import DPSDiscordClient
from funnyboard.twitter.client import TwitterAPIClient


def main():
    intents = discord.Intents.default()
    intents.message_content = True
    discord.utils.setup_logging()

    twitter_api = TwitterAPIClient(
        client=TWITTER_CONSUMER_KEY,
        client_secret=TWITTER_CONSUMER_SECRET,
        token=TWITTER_ACCESS_KEY,
        secret=TWITTER_ACCESS_SECRET
    )
    client = DPSDiscordClient(intents=intents, twitter_client=twitter_api)

    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()
