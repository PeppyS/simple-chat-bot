import json
import unittest
from unittest.mock import patch, mock_open

from bot import BotConfig, Bot


class TestBotConfig(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open,
           read_data=json.dumps({'commands': [{'triggers': ['bot test'], 'response': 'sup'}]}))
    def test_from_json_file(self, _):
        config = BotConfig.from_json_file('fake_config_path.json')

        self.assertEqual(config.commands, [{'triggers': ['bot test'], 'response': 'sup'}])


class TestBot(unittest.TestCase):

    def test_get_response(self):
        bot_config = BotConfig()
        bot_config.commands = [{
            'triggers': ['bot test'],
            'response': 'sup'
        }]
        bot = Bot(bot_config)

        response = bot.get_response('bot test')
        self.assertEqual(response, 'sup')


if __name__ == '__main__':
    unittest.main()
