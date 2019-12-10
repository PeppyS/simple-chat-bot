import json
from enum import Enum
from typing import List, Optional


class ResponseType(Enum):
    Text = 'TEXT'
    DadJoke = 'DAD_JOKE'


class Response:
    type: ResponseType
    value: Optional[str]


class Command:
    triggers: List[str]
    response: Response


class BotConfig:
    commands: List[Command]

    @staticmethod
    def from_json_file(path: str):
        with open(path) as json_file:
            commands = json.load(json_file)
            bot_config = BotConfig()

            # TODO - add validation
            bot_config.commands = commands

            return bot_config
