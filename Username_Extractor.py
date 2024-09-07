from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsRecent

# Replace with your API credentials and phone number
api_id = 'API ID'
api_hash = 'API HASH'
phone_number = 'NUMBER' # International format, same as logging into my.telegram.org
group_username = 'GROUP USERNAME'  # or use the group ID

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone_number)

    # Getting the group entity
    group = await client.get_entity(group_username)

    # Initialize variables for pagination
    offset = 0
    limit = 100
    all_users = []

    while True:
        # Fetching participants
        response = await client(GetParticipantsRequest(
            channel=group,
            filter=ChannelParticipantsRecent(),
            offset=offset,
            limit=limit,
            hash=0  # Provide a dummy value for the hash parameter
        ))

        # Append users to the list
        all_users.extend(response.users)
        
        # Check if we've fetched all users
        if len(response.users) < limit:
            break
        
        # Update offset for the next batch
        offset += limit

    # Find the number of participants
    num_participants = len(all_users)
    print(f"Number of participants: {num_participants}")

    # Save participant usernames to a file
    with open('usernames.txt', 'w') as file:
        for participant in all_users:
            username = participant.username
            first_name = participant.first_name
            last_name = participant.last_name or ''
            if username:
                file.write(f"@{username}\n")
            else:
                file.write(f"{first_name} {last_name}\n")

    print("Usernames have been saved to 'usernames.txt'.")

with client:
    client.loop.run_until_complete(main())