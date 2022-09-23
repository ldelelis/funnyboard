from pydantic import BaseModel


class TwitterAPIRequest(BaseModel):
    text: str


class TwitterAPIResponse(BaseModel):
    id: str
    text: str
