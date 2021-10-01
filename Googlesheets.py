import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
import sys
import csv
import random
import time
import json
api_id = 1516198
api_hash = "2247052f4f427e7c44070eaf74c02f6a"
phone = "+12403546115"
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("MyProject-03e17d26dccf.json", scope)
clientz = gspread.authorize(creds)
sheet = clientz.open("TestingDatabase").sheet1
data = sheet.get_all_records()

input_file = sys.argv[1]
user = {}
with open(input_file, encoding='UTF-8') as f:
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        ID = int(row[1])
        user[ID] = int(row[2])

for elem in data:
    UserID =  elem['Telegram User ID']
    messages = json.dumps(elem, indent=1)
    receiver = InputPeerUser(UserID, user[UserID])
    print("Sending Message to:", elem['Karyakar Name'])
    client.send_message(receiver, messages)

client.disconnect()
print("Done. Message sent to all users.")
