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
- Telegram bot's bot token (optional depending on your approach below)

To obtain an API ID and API Hash:
  Go to [my.telegram.org]([https://my.telegram.org/]) and log in. Click on **App Development Tools** and create a new app.

To obtain the group_username for private groups, there are two options.
The first option would be to go to telegram web and select the group. 
In the link, you should then see "https://web.telegram.org/a/#{group-number-here}". You can extract the group number, including the "-" sign if present.

The second option would be to create a new bot:
  1. Create a new bot using @BotFather and obtain the bot token.
  2. Add the bot to the group and give it admin privileges.
  3. Run the command in the group "/getgroupid".

The group username for public groups are @groupname. Simply key in "groupname".

To run the application:
python Username_Extractor.py and the usernames will be saved in a text file called usernames.txt
