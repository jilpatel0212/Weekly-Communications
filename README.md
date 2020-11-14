# Weekly-Communications

Description: The developed Python script utilized Telethon (Telegram) and Google Sheets API. It was used to send information in a row of google sheets to a particualr telegram user extracted from a group. The information was sent to the user whose user ID was listed in the google sheets.

getUserInfo.py extracts all of the telegram user's in a group and stores in a CSV file.

Googlesheets.py iterates through the google sheets which has information that needs to be sent to the telegram user. It also contains the user ID that was extracted from getUserInfo.py
