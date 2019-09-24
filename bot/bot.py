import json
import re
from typing import List, Optional

from chat_provider import ChatProvider


class BotConfig:
    commands: List

    @staticmethod
    def from_json_file(path):
        with open(path) as json_file:
            commands = json.load(json_file)
            bot_config = BotConfig()

            # TODO - add validation
            bot_config.commands = commands

            return bot_config


class Bot:
    def __init__(self, config: BotConfig, chat_provider: ChatProvider):
        self.config = config
        self.chat_provider = chat_provider

    def handle_message(self, message: str) -> Optional[str]:
        response = self.__get_response(message)

        if response is not None:
            self.chat_provider.send_message(response)

        return response

    def __get_response(self, message: str) -> Optional[str]:
        # Remove non-alphanumeric characters and whitespaces
        message_normalized = re.sub(r'[^\w]', ' ', message).strip().lower()

        command = list(filter(lambda x: message_normalized in x['triggers'], self.config.commands))
        if len(command) == 0:
            return None

        return command[0]['response']
