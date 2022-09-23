from typing import Any
from discord.client import Client
from discord.flags import Intents
from discord.message import Message

from funnyboard.config import STARBOARD_CHANNEL_ID
from funnyboard.twitter.client import TwitterAPIClient


class DPSDiscordClient(Client):
    def __init__(self, *, intents: Intents, twitter_client: TwitterAPIClient, **options: Any) -> None:
        super().__init__(intents=intents, **options)
        self.twitter_client = twitter_client

    async def on_message(self, message: Message):
        if message.channel.id != int(STARBOARD_CHANNEL_ID):
            return

        embed = message.embeds[0]
        if embed.image:
            return

        content = embed.description
        if content:
            self.twitter_client.tweet(content)
