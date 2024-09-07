# TelegramGroupUsernameExtractor
Extract the usernames of all members in a Telegram group

Required libraries:
  1. telethon
  2. telegram

Required information:
- API ID
- API Hash
- phone number to log into Telegram account
- group chat username
- Telegram bot's bot token

To obtain an API ID and API Hash:
  Go to [my.telegram.org]([https://my.telegram.org/]) and log in. Click on **App Development Tools** and create a new app.

To obtain the group_username for private groups:
  1. Create a new bot using @BotFather and obtain the bot token.
  2. Add the bot to the group and give it admin privileges.
  3. Run the command in the group "/getgroupid".
     
The group username for public groups are @groupname. Simply key in "groupname".

To run the application:
python Username_Extractor.py and the usernames will be saved in a text file called usernames.txt


Future Planned Improvements:
- Find a way to get group chat username without creating and adding a bot to the group.
