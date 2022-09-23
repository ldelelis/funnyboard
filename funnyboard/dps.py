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
        print("on receiver")
        if message.channel.id != int(STARBOARD_CHANNEL_ID):
            print("skipped")
            print(f"expected id: {STARBOARD_CHANNEL_ID}")
            print(f"got id: {message.channel.id}")
            return

        embed = message.embeds[-1]
        if embed.image:
            print("got image")
            return

        content = embed.description
        if content:
            resp = self.twitter_client.tweet(content)
            print(f"got resp {resp.status_code}, {resp.json()}")
