import re
from typing import Optional

from bot.dad_joke import get_dad_joke
from bot.config import BotConfig, ResponseType
from chat_provider import ChatProvider
from chat_provider.chat_provider import ChatProviderSource


class Bot:
    def __init__(self, config_path: str, chat_provider: ChatProviderSource):
        self.config = BotConfig.from_json_file(config_path)
        self.chat_provider = ChatProvider.get_client(provider=chat_provider)

    def handle_message(self, message: str) -> Optional[str]:
        response = self.__get_response(message)

        if response is not None:
            self.chat_provider.send_message(response)

        return response

    def __get_response(self, message: str) -> Optional[str]:
        # Remove non-alphanumeric characters and whitespaces
        message_normalized = re.sub(r'[^\w]', ' ', message).strip().lower()

        command = list(filter(lambda x: message_normalized in x.triggers, self.config.commands))
        if len(command) == 0:
            return None

        response = command[0].response
        if response.type == ResponseType.Text:
            return response.type
        elif response.type == ResponseType.DadJoke:
            return get_dad_joke()
        else:
            raise ValueError(f'Unrecognizable type: {response.type}')
