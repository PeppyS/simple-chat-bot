from flask import Request, jsonify
import os
from bot import BotConfig, Bot
from chat_provider.group_me import GroupMeClient, GroupMeWebhookMessage

# TODO - Validate bot_config.json exists and env GROUP_ME_BOT_ID is set
bot_config = BotConfig.from_json_file(path='bot_config.json')
group_me_client = GroupMeClient(bot_id=os.getenv('GROUP_ME_BOT_ID'))
bot = Bot(config=bot_config, chat_provider=group_me_client)


def handle_group_me_message(request: Request):
    json = request.get_json(force=True)
    message = GroupMeWebhookMessage.from_dict(json or {})

    print(f'Received new GroupMe message: {message.__dict__}')

    response = bot.handle_message(message.text)

    print({
        'text': message.text,
        'response': response,
    })

    return jsonify({'success': True, 'response': response})
