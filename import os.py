import os
from slack import WebClient
from slack.errors import SlackApiError
# Set your Slack Bot User OAuth Access Token
slack_token = 'xoxb-5865651330082-6040409364822-zpLXhtmqvrjkiIxcsLhILu78'
client = WebClient(token=slack_token)
# Eldralin Universe custom responses
responses = {
    "lore": "In the ancient lore of Eldralin, it is said that the world was born from the convergence of five primal elements.",
    "magic": "The magic of Eldralin flows through every living being, connecting the realms in an intricate web of mystical energy.",
    "creatures": "Eldralin is teeming with a myriad of creatures, from the graceful unicorns of the Whispering Glades to the fearsome dragons of the Ember Peaks."
}
# Slack event handling
@slack.RTMClient.run_on(event='message')
def respond_to_user(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if 'text' in data and 'bot_id' not in data:
        channel_id = data['channel']
        user = data['user']
        text = data['text']
        text_lower = text.lower()
        if 'eldralin' in text_lower:
            if 'lore' in text_lower:
                send_response(web_client, channel_id, responses["lore"])
            elif 'magic' in text_lower:
                send_response(web_client, channel_id, responses["magic"])
            elif 'creatures' in text_lower:
                send_response(web_client, channel_id, responses["creatures"])
# Function to send response
def send_response(web_client, channel_id, message):
    try:
        web_client.chat_postMessage(
            channel=channel_id,
            text=message
        )
    except SlackApiError as e:
        assert e.response['ok'] is False
        assert e.response['error']
# Connect to the Slack RTM API
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start() (edited) 
