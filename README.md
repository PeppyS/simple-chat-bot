# chatty
Currently only supports GroupMe and Google Cloud Functions.

## Prerequisites
- A GroupMe developer account and bot ID: https://dev.groupme.com/
- A GCP account, with gcloud CLI installed: https://cloud.google.com/sdk/gcloud/

## Setup
```shell
# Clone and go to directory
git clone git@github.com:PeppyS/chatty.git
cd chatty

# Create your bot configuration file
echo '[
  {
    "triggers": ["yo", "sup", "whats up"],
    "response": {
      "type": "TEXT",
      "value": "Nothing much, you?"
    }
  }
]' >> bot_config.json

# Deploy your cloud function
FUNCTION_NAME=handle_group_me_message PROJECT_ID=your-gcp-project-id GROUP_ME_BOT_ID=your-bot-id ./bin/deploy-gcp-function
```

## Bot Configuration
Pretty dumb configuration file that takes a list of commands, containing a list of triggers and responses.
```json
[
  {
    "triggers": ["yo", "sup", "whats up"],
    "response": {
      "type": "TEXT",
      "value": "Nothing much, you?"
    }
  },
  {
    "triggers": ["joke", "dad joke"],
    "response": {
      "type": "DAD_JOKE"
    }
  }
]
```

Hopefully this will eventually support other types of commands.
