import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from tabulate import tabulate
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

##def print_formatted(data):
  #  for item, amount s
#print(list(data))
#df = pd.read_csv("members.csv")
#kar_list = list(data[indent=1])
#close_list = list(data['userID'])
#perfect_dict = []

#take_lenght = min(len(kar_list), len(close_list))
#for i in take_lenght:
 #   temp_dict = {}
  #  temp_dict['Karykar Name'] = kar_list[i]
   # temp_dict['userID'] = close_list[i]
    #perfect_dict.append(temp_dict)
#print(perfect_dict)
#print(type(data))
res = []
for idx, sub in enumerate(data, start = 0):
    if idx == 0:
        res.append(list(sub.keys()))
        res.append(list(sub.values()))
    else:
        res.append(list(sub.values()))
#new = []
#for r in zip(res):
  #  new.append(*r)
 #   print(new)
#print(str(res))
#print(res)
#print(tabulate(res))
#length_list = [len(element) for row in res for element in row]
#columnn_width = max(length_list)
#for row in res:
#    row = "".join(element.ljust(column_width + 2) for element in row)
new = []
for k in range(len(res[0])):
    for v in range(len(res)):
        new.append(res[v][k])
        print(res[v][k], end = ' ')
    print()
print(new)



for elem in data:
    UserID =  elem['Telegram User ID']
    messages = str(res)#str(elem).replace("{","").replace("}", "")
    send_me = json.dumps(messages, indent = 1)
    #print(send_me)
    #messages = json.dumps(elem, indent=1)
    
    
    receiver = InputPeerUser(UserID, user[UserID])
    print("Sending Message to:", elem['Karyakar Name'])
    client.send_message(receiver, messages)

client.disconnect()
print("Done. Message sent to all users.")