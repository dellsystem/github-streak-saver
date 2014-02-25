GitHub Streak Saver
===================

Your daily reminder to keep up that contribution streak.

Inspired by <https://ryanseys.com/blog/177-days-of-github/>. I'm aiming for at
least 178.

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

You really only need one line in your crontab, if you want to make it a daily
reminder. But if you're like me, then you probably don't think that a single
reminder a day is sufficient. Here's what my crontab looks like:

```crontab
0 18 * * * /edit/this/send_sms.py "You haven't committed yet!"
0 19 * * * /edit/this/send_sms.py "Still haven't committed ..."
0 20 * * * /edit/this/send_sms.py "It's already 8 and you STILL haven't committed??"
0 21 * * * /edit/this/send_sms.py "What are you waiting for? Commit already!"
0 22 * * * /edit/this/send_sms.py "Just like open an issue or something come on"
0 23 * * * /edit/this/send_sms.py "I don't know what you're waiting for. Do you want to keep up your streak or not?"
0 0 * * * /edit/this/send_sms.py "It's midnight. You're lucky Github uses PST."
0 1 * * * /edit/this/send_sms.py "I hope you're still awake because you have 2 hours to commit something."
0 2 * * * /edit/this/send_sms.py "It doesn't have to be good, just don't break your streak please"
45 2 * * * /edit/this/send_sms.py "You have 15 minutes to save your streak"
59 2 * * * /edit/this/send_sms.py "1 minute left ... don't fuck up"
```

(Edit with `crontab -e`.)

Licensing
---------

MIT license.
