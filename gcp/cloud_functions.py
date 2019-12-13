from flask import Request, jsonify
from bot import Bot

from chat_provider.chat_provider import ChatProviderSource
from chat_provider.group_me import GroupMeWebhookMessage

bot = Bot(config_path='bot_config.json', chat_provider=ChatProviderSource.GroupMe)


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
