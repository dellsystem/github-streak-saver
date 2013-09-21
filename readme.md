Your daily SMS reminder to commit to Github
===========================================

CAN'T BREAK THAT STREAK

Requirements
------------

Requires Python 2.7. You can get the needed dependencies via `pip install -r
requirements.txt`.

Installation instructions
-------------------------

Edit conf.py. Should be self-explanatory. If you don't have a Twilio account
already, you can get a free trial [here](https://www.twilio.com/try-twilio).
Note that you'll have to activate your phone number before you'll be able to
receive messages on that phone.

Setting up your crontab
-----------------------

0 18 * * * /edit/this/send_sms.py "You haven't committed yet!"
0 19 * * * /edit/this/send_sms.py "Still haven't committed ..."
0 20 * * * /edit/this/send_sms.py "It's already 8 and you STILL haven't committed??"
0 21 * * * /edit/this/send_sms.py "What are you waiting for? Commit already!"
0 22 * * * /edit/this/send_sms.py "Just like open an issue or something come on"
0 23 * * * /edit/this/send_sms.py "I don't know what you're waiting for. Do you want to keep up your streak or not?"
0 24 * * * /edit/this/send_sms.py "It's midnight. You're lucky Github uses PST."
0 1 * * * /edit/this/send_sms.py "I hope you're still awake because you have 2 hours to commit something."
0 2 * * * /edit/this/send_sms.py "It doesn't have to be good, just don't break your streak please"
0 3 * * * /edit/this/send_sms.py "You fucked up"
