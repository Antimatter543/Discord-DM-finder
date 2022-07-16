# Discord DM Finder


I made this because I couldn't find another solution online, other than one where you had to download an .exe from a google drive.

## How to use
Download your Discord Package, and unzip it in this directory, placing 'packages' at the same level as this README and main.py.


### Step 1
Create a constants.py file on the directory, and add
```
MY_ID = XXXXXXXXXXXXXXXXXX

### Only if you want to filter against closed messages. Otherwise, leave like this.
DISCORD_EMAIL = ''
PASSWORD = ''
CHROMEDRIVER_PATH = ""

```

1. Run main.py

2. Comb through the IDs and check them on a DISCORD id lookup site (the guru site is good).
4.With the id, go into a server (any server of yours, or a chill one), and type <@IDnumber>.
5. Press enter.
6. Sometimes, if they've blocked you or weird things are happening, it will stay as the number. Do not fret. Log onto discord on the browser *as well*, and try it again. Hopefully, it should converge back to their actual username. 

7. Right click on the blue name, then click "Message".
8. It should open your closed dms again. Type anything so discord adds this into your DM list again, and voila! (You can delete the dot if you want, the DM won't go away until you click X again).
:) 

### DEBUG - If something doesn't work
Chances are, you might run into problems for the opened_messages.py
If your login details are working and you see the browser get to your DM screen, but nothing happens, try increasing the numbers in time.sleep().