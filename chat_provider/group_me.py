import requests

from chat_provider.chat_provider import ChatProvider


class GroupMeClient(ChatProvider):
    post_endpoint: str = 'https://api.groupme.com/v3/bots/post'
    bot_id: str

    def __init__(self, bot_id: str):
        self.bot_id = bot_id

    def send_message(self, message: str):
        response = requests.post(self.post_endpoint, data={'bot_id': self.bot_id, 'text': message})
        response.raise_for_status()


class GroupMeWebhookMessage:
    group_id: str
    name: str
    sender_type: str
    text: str

    @staticmethod
    def from_dict(d: dict):
        m = GroupMeWebhookMessage()
        m.__dict__ = d  # TODO - add validation

        return m
