from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# Configure your API credentials
api_id = 'api_code'
api_hash = 'api_hash'

# Configure your session file name
session_name = 'session_file_name'

# Configure the target channel username or ID
channel_link  = "int user ID"

# Initialize the Telegram client
client = TelegramClient(session_name, api_id, api_hash)
client.start()



channel = client.get_entity(channel_link)
messages = client.get_messages(channel, limit=1000)  # You can change the limit as needed


# for message in messages:
with open('channel_messages.txt', 'w', encoding='utf-8') as file:
    for message in messages:
        file.write(message.text + '\n')

        print(message.text)


client.disconnect()

#     # Save messages to a file

