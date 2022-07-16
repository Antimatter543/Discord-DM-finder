import json
import os
from helpers import *
from constants import MIN_ROWS, MY_ID
from pprint import pprint


message_list = os.listdir('package/messages/')
# print("Files and directories in messages directory :")
# print(message_list) # List

# Does operations within the 'packages/messages/' directory.
# List of people who we care about -- everyone who's a DM, everyone who's filtered.
dm_ids = {'other': {}, 'filtered_dms': {}}
direct_messages = {}

for message in message_list:
    # print("we're in here now")
    filename = os.fsdecode(message)
    # Lets us easily access all XXXX messages and not worry about index.json
    if not filename.endswith(".json"):
        channel_path = 'package/messages/'+message+'/channel.json'
        messages_path = 'package/messages/'+message+'/messages.csv'
        # Do stuff to things we know are private dms
        if message_is_dm(channel_path):
            with open(channel_path, 'r') as channel, open(messages_path, 'r', encoding='utf-8') as messages:

                ### CHANNEL ###
                data = json.load(channel)
                # Get data out of them.
                recipients = data['recipients']
                recipients.remove(str(MY_ID))
                their_id = recipients[0]
                message_id = data['id']  # Channel / message ID

                ### CSV ###
                content = messages.readlines()
                # Cursed code that just gets the date -- last line (oldest message), split, second comma (date), split, first section (date no 24hr time)
                oldest_message = content[-1].split(',')[1].split(' ')[0]
                num_rows = len(content[1:])

                # Add data to dictionary
                direct_messages[message_id] = {"recipient": their_id, "first_messaged": oldest_message,
                                               "message_folder": "package/messages/"+message+'/', "num_messages": num_rows}

while True:
    # Create the message dicts
    length_filter = int(
        input("Minimum length of message history (only counts your messages): "))
    filtered_dms = get_dms_greater_than(direct_messages, length_filter)
    closed_messages = {}
    closed_filtered_messages = {}
    if os.stat('data.txt') != 0: # Create filtered dms if data not empty
        closed_messages = get_closed_dms(direct_messages)
        closed_filtered_messages = get_closed_dms(filtered_dms)

    # Ask user what type of dictionary they want

    try:
        ask = int(input(f"""What do you want to see? Shown in effectively oldest-newest order.
    \n1: Everything (Dict contains {len(direct_messages)} message IDs)
    \n2: All DMS with length filter (Dict contains {len(filtered_dms)} message IDs)
    \n3: All closed DMS (Dict contains {len(closed_messages)} message IDs) | Needs data.txt
    \n4: All closed + filtered dms (Dict contains {len(closed_filtered_messages)} message IDs) | Needs data.txt
    \nType the number of your chosen option : """))
    except ValueError:
        print("Try again, that's not an integer")
        continue

    if ask == 1:
        pprint(direct_messages)
    elif ask == 2:
        pprint(filtered_dms)
    elif ask == 3:
        pprint(closed_messages)
    elif ask == 4:
        pprint(closed_filtered_messages)
    else:
        print("Try again -- Type a number from 1-4.")