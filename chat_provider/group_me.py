import requests

from chat_provider.chat_provider import ChatProvider


class GroupMeClient(ChatProvider):
    def __init__(self, bot_id: str):
        self.bot_id = bot_id
        self.post_endpoint = 'https://api.groupme.com/v3/bots/post'

    def send_message(self, message: str):
        response = requests.post(self.post_endpoint, data={'bot_id': self.bot_id, 'text': message})
        response.raise_for_status()


class GroupMeWebhookMessage:
    def __init__(self, group_id: str, name: str, sender_type: str, text: str):
        self.group_id = group_id
        self.name = name
        self.sender_type = sender_type
        self.text = text

    @staticmethod
    def from_dict(d: dict):
        for required_key in ['group_id', 'name', 'sender_type', 'text']:
            if required_key not in d:
                raise TypeError(f'Required key {required_key} not found in dict {d}')

        return GroupMeWebhookMessage(group_id=d.get('group_id'), name=d.get('name'),
                                     sender_type=d.get('sender_type'), text=d.get('text'))
