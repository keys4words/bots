import configparser
import json
from datetime import date, datetime

from telethon.sync import TelegramClient
from telethon import connection


# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest



config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

client = TelegramClient(username, api_id, api_hash)
client.start()


async def dump_all_participants(channel):
    offset_user = 0
    limit_user = 100
    all_participants = []
    filter_user = ChannelParticipantsSearch('')

    while True:
        participants = await client(GetParticipantsRequest(channel, filter_user, offset_user, limit_user, hash=0))
        if not participants.users:
            break
        all_participants.extend(participants.users)
        offset_user += len(participants.users)

    all_users_details = []
    for participant in all_participants:
        all_users_details.append({"id": participant.id,
			"first_name": participant.first_name,
			"last_name": participant.last_name,
			"user": participant.username,
			"phone": participant.phone,
			"is_bot": participant.bot})
    with open('channel_users.json', 'w', encoding='utf8') as f:
        json.dump(all_users_details, f, ensure_ascii=False)



async def main():
    url = input('Input url of telegram chat or channel: ')
    channel = await client.get_entity(url)
    await dump_all_participants(channel)
    # await dump_all_messages(channel)


with client:
    client.loop.run_until_complete(main())