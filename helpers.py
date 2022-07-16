import json
from copy import deepcopy
def message_is_dm(filepath: str ) -> bool:
    """ Checks if a given message folder is a direct message

    Args:
        filepath (str): Filepath to the message's channel json; i.e
        "package/messages/XXXXXX.../channel.json"

    Returns:
        bool: Bool of whether the messages are private dms or not.
    """
    with open(filepath) as channel:
        data = json.load(channel)
        return data['type'] == 1 ## If the type is 1 that's a direct message (dm)


def get_closed_dms(dms: dict) -> None:
	""" Returns messages that aren't accessible from your opened Discord DMS 
	
	ONLY WORKS IF opened_messages.py ran successfully and made a data.txt.

	Args:
		dms (Dict[str, Dict[str, str, str, int]]): Direct_Messages = {
message_id: {recipient:. str, first_messaged: str, message_folder: str, num_messages: int}, 
...}

	Returns:
		dict: A same type dictionary of closed dms only.
	"""
	return_dict = deepcopy(dms)
	with open('data.txt', 'r') as data:
		open_dms = json.load(data)

	# Remove opened DM ids from DM dict
	for message_id in open_dms:
		asscheeks = return_dict.pop(message_id, None) 
	
	return return_dict

def get_dms_greater_than(dms: dict, length: int) -> dict:
	""" Returns a dictionary with message info about any message folders that have > Length messages sent by you.

	Args:
		dms (Dict): direct messages dictionary 
		length (int): Minimum length of messages

	Returns:
		dict:direct messages dictionary 
	"""
	return_dict = deepcopy(dms)
	for key, val in dms.items():
		if val['num_messages'] < length:
			del return_dict[key]


	return return_dict