from requests import Session
from requests_oauthlib import OAuth1Session
from requests_oauthlib.oauth1_auth import OAuth1

from funnyboard.twitter.schema import TwitterAPIRequest


class TwitterAPIClient(Session):
    def __init__(self, token=None, secret=None, client=None, client_secret=None) -> None:
        super().__init__()
        self.url = "https://api.twitter.com/2"
        self.token = token
        self.secret = secret
        self.client = client
        self.client_secret = client_secret

    def __auth(self):
        return OAuth1(self.client, self.client_secret, self.token, self.secret)

    def __get_headers(self):
        return {
            "Content-Type": "application/json",
        }

    def tweet(self, content: str):
        body = TwitterAPIRequest(text=content)
        headers = self.__get_headers()
        auth = self.__auth()

        response = self.post(f"{self.url}/tweets", json=body.dict(), headers=headers, auth=auth)
        response.raise_for_status()
