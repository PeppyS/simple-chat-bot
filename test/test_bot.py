import json
import unittest
from unittest import mock
from unittest.mock import patch, mock_open

from bot import BotConfig, Bot
from bot.config import ResponseType
from chat_provider.chat_provider import ChatProviderSource, ChatProvider


class TestBotConfig(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open,
           read_data=json.dumps(
               [{'triggers': ['bot test', 'bot testt'],
                 'response': {'type': 'TEXT', 'value': 'sup'}}]))
    def test_from_json_file(self, _):
        config = BotConfig.from_json_file('fake_config_path.json')

        assert len(config.commands) == 1
        assert config.commands[0].triggers == ['bot test', 'bot testt']
        assert config.commands[0].response.type == ResponseType.TEXT
        assert config.commands[0].response.value == 'sup'


class TestBot(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open,
           read_data=json.dumps([{
               'triggers': ['test trigger 1', 'test trigger 2'],
               'response': {'type': 'TEXT', 'value': 'sup'}
           }]))
    def test_get_response(self, _):
        with mock.patch.object(ChatProvider, 'get_client'):
            bot = Bot(config_path='fake_config_path.json', chat_provider=ChatProviderSource.GroupMe)

            command = bot.config.commands[0]
            attempts = command.triggers
            # uppercase
            attempts.extend(list(map(lambda x: x.upper(), command.triggers)))
            # lowercase
            attempts.extend(list(map(lambda x: x.lower(), command.triggers)))
            # spaces
            attempts.extend(list(map(lambda x: "    " + x + " ", command.triggers)))

            for trigger in command.triggers:
                response = bot.handle_message(trigger)

                assert response == command.response.value
                bot.chat_provider.send_message.assert_called_with(response)
