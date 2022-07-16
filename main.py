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

                # # Filter
                # if num_rows > MIN_ROWS:
                # 	dm_ids['filtered_dms'][message_id] = {"recipient": their_id, "first_messaged": oldest_message, "message_folder": message, "num_messages": num_rows }
                # else:
                # 	# Any non filtered stuff (if you wanted to use it)
                # 	dm_ids['other'][message_id] = {"recipient": their_id, "first_messaged": oldest_message, "message_folder": message, "num_messages": num_rows }

# pprint(direct_messages)
length_filter = int(
    input("Minimum length of message history (only counts your messages): "))
filtered_dms = get_dms_greater_than(direct_messages, length_filter)

# print("Number of DMs found in total:", (len(direct_messages)),
    #   "Number of DMS with larger length than", length_filter, ":", len(filtered_dms))

# if input("Do you want to only see messages you've closed? y/n") == 'y':
closed_messages = {}
closed_messages = get_closed_dms(direct_messages)
closed_filtered_messages = get_closed_dms(filtered_dms)

# pprint(closed_filtered_messages)
# print(
#     f"Length of just closed messages (no min length filter): {len(closed_messages)}, Length of closed + filtered messages: {len(closed_filtered_messages)}")

while True:
    ask = int(input(f"""What do you want to print? \n
    1: Everything(Dict contains {len(direct_messages)} message IDs)
    \n2: All DMS with length filter (Dict contains {len(filtered_dms)} message IDs)
    \n3: All closed DMS (Dict contains {len(closed_messages)} message IDs)
    \n4: All closed + filtered dms (Dict contains {len(closed_filtered_messages)} message IDs)
    \nType a number: """))
    if ask == 1:
        pprint(direct_messages)
    elif ask == 2:
        pprint(filtered_dms)
    elif ask == 3:
        pprint(closed_messages)
    else:
        pprint(closed_filtered_messages)
