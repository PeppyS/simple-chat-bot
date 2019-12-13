import json
from enum import Enum
from typing import List, Optional


class ResponseType(Enum):
    TEXT = 'TEXT'
    DAD_JOKE = 'DAD_JOKE'

    @staticmethod
    def list() -> List[str]:
        return [rt.value for rt in ResponseType]


class Response(object):
    def __init__(self, type: ResponseType, value: Optional[str]):
        self.type = type
        self.value = value


class Command(object):
    def __init__(self, triggers: List[str], response: Response):
        self.triggers = triggers
        self.response = response


class BotConfig(object):
    def __init__(self, commands: List[Command]):
        self.commands = commands

    @staticmethod
    def from_json_file(path: str):
        with open(path) as json_file:
            config_json = json.load(json_file)
            commands = []

            if not isinstance(config_json, list):
                raise TypeError('Expected list of commands')

            for command_dict in config_json:
                if not isinstance(command_dict, dict):
                    raise TypeError('Expected list of commands to be dicts')

                if 'triggers' not in command_dict or not isinstance(command_dict['triggers'], list):
                    raise TypeError('Expected each command to have key "triggers" as list')
                if 'response' not in command_dict or not isinstance(command_dict['response'], dict):
                    raise TypeError('Expected each command to have key "response" as dict')

                response_dict = command_dict['response']
                if not isinstance(response_dict, dict):
                    raise TypeError('Expected response to be dict')
                if 'type' not in response_dict or response_dict['type'] not in ResponseType.list():
                    raise TypeError(
                        f'Expected each command to have either response type {ResponseType.list()}')
                if 'value' in response_dict and not isinstance(response_dict['value'], str):
                    raise TypeError('Expected response value to be str if set')

                response = Response(type=ResponseType(response_dict['type']),
                                    value=response_dict.get('value', None))
                command = Command(triggers=command_dict['triggers'], response=response)
                commands.append(command)

            return BotConfig(commands=commands)
