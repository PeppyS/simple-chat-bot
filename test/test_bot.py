import json
import unittest
from unittest.mock import patch, mock_open

from bot import BotConfig, Bot


class TestBotConfig(unittest.TestCase):
    commands = [{'triggers': ['bot test'], 'response': 'sup'}]

    @patch("builtins.open", new_callable=mock_open,
           read_data=json.dumps(commands))
    def test_from_json_file(self, _):
        config = BotConfig.from_json_file('fake_config_path.json')

        self.assertEqual(config.commands, self.commands)


class TestBot(unittest.TestCase):

    def test_get_response(self):
        bot_config = BotConfig()
        command = {
            'triggers': ['test trigger 1', 'test trigger 2'],
            'response': 'sup'
        }
        bot_config.commands = [command]
        chat_provider = unittest.mock.Mock()
        bot = Bot(config=bot_config, chat_provider=chat_provider)

        attempts = command['triggers']
        # uppercase
        attempts.extend(list(map(lambda x: x.upper(), command['triggers'])))
        # lowercase
        attempts.extend(list(map(lambda x: x.lower(), command['triggers'])))
        # spaces
        attempts.extend(list(map(lambda x: "    " + x + " ", command['triggers'])))

        for trigger in command['triggers']:
            response = bot.handle_message(trigger)
            self.assertEqual(response, command['response'])
            chat_provider.send_message.assert_called_with(response)
