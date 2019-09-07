# simple-chat-bot
Currently only supports GroupMe and Google Cloud Functions.

## Prerequisites
- A GroupMe developer account and bot ID: https://dev.groupme.com/
- A GCP account, with gcloud CLI installed: https://cloud.google.com/sdk/gcloud/

## Setup
```shell
# Clone and go to directory
git clone git@github.com:PeppyS/simple-chat-bot.git
cd simple-chat-bot

# Create your bot configuration file
echo '{
  "commands": [
    {
      "triggers": ["yo", "sup", "whats up"],
      "response": "Nothing much, you?"
    }
  ]
}' >> bot_config.json

# Deploy your cloud function
FUNCTION_NAME=handle_group_me_message PROJECT_ID=your-gcp-project-id GROUP_ME_BOT_ID=your-bot-id ./bin/deploy-gcp-function
```

## Bot Configuration
Pretty dumb configuration file that takes a list of commands, containing a list of triggers and responses.
```json
{
  "commands": [
    {
      "triggers": ["yo", "sup", "whats up"],
      "response": "Nothing much, you?"
    }
  ]
}

```

Hopefully this will eventually support more dynamic commands, like API calls.