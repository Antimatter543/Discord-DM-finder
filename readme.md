# Discord DM Finder
Ever wanted to find someone's DMs with you again, if you had already closed them and blocked them, or are no longer friends with them? This solves that!


I made this [Discord DM Finder](https://discord.com/) because I couldn't find another solution online, other than one where you had to download an .exe from a google drive. 
The script helps you locate all messages, including message histories that you have closed before and can't open (i.e you don't remember their ID or name, and aren't friends).
Tested on Windows.

## Instructions
1. Download your Discord Package, and unzip it in this directory, placing 'packages' at the same level as this README and main.py.
2. Make a venv and type ```pip install requirements.txt``` into terminal.
3. Create a constants.py file on the directory, and put the below into it, replacing the XXX's with your discord ID. If you do not want to filter against closed messages, don't touch the other variables.
```
MY_ID = XXXXXXXXXXXXXXXXXX

### Only if you want to filter against closed messages. Otherwise, leave like this.
DISCORD_EMAIL = ''
PASSWORD = ''
CHROMEDRIVER_PATH = ""
```
3. OPTIONAL: Run opened_messages.py* -- a successful run results in the data.txt file.

4. Run main.py and get the information you want.

5. Figure out who you're looking for - can compare first date messaged, look at each message.csv file, or lookup their discord ID on a lookup site.

6.  With the ID you want, go into a server (any server of yours, or a chill one), and type <@IDnumber>.

7. Press enter.

8. Sometimes, it will stay as the number. Do not fret. Log onto discord on the browser *as well*, and try it again. Hopefully, it should converge back to their actual username. 

9. Right click on the blue name, then click "Message".

10. It should open your closed dms again. Type anything so discord adds this into your DM list again, and voila! (You can delete the dot if you want, the DM won't go away until you click X again).


## DEBUG - If something doesn't work
Opened_messages.py is optional because the only way I figured out how to get a list of 'closed messages', is to get to your current messages and subtract that from all messages. You can manually comb through all the data yourself if you want without running it.

Chances are, you might run into problems for the opened_messages.py
If your login details are working and you see the browser get to your DM screen, but nothing happens, try increasing the numbers in time.sleep(). I didn't know a way around this, (send me a message if you do), but basically your browser doesn't load the DM screen fast enough.
