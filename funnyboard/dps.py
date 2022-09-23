import re
from typing import Any

from discord.client import Client
from discord.flags import Intents
from discord.message import Message

from funnyboard.config import STARBOARD_CHANNEL_ID, TWEETS_ENABLED
from funnyboard.twitter.client import TwitterAPIClient


class DPSDiscordClient(Client):
    def __init__(self, *, intents: Intents, twitter_client: TwitterAPIClient, **options: Any) -> None:
        super().__init__(intents=intents, **options)
        self.twitter_client = twitter_client

    async def on_message(self, message: Message):
        if message.channel.id != int(STARBOARD_CHANNEL_ID):
            return

        import ipdb; ipdb.set_trace()
        embed = message.embeds[-1]
        if embed.image:
            return

        content = re.sub(r"<@.*>", "@anon", embed.description)
        if not content:
            return

        if TWEETS_ENABLED:
            resp = self.twitter_client.tweet(content)
