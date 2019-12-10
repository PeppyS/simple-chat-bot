import os
from abc import ABC, abstractmethod
from enum import Enum

from chat_provider import GroupMeClient


class ChatProviderSource(Enum):
    GroupMe = 'group_me'


class ChatProvider(ABC):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass

    @staticmethod
    def get_client(provider: ChatProviderSource) -> 'ChatProvider':
        if provider == ChatProviderSource.GroupMe:
            return GroupMeClient(bot_id=os.getenv('GROUP_ME_BOT_ID'))
        else:
            raise Exception(f'No client found for provider {provider}')
