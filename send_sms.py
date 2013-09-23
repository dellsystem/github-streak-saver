#!/usr/bin/env python

import json
import sys

import requests
from twilio.rest import TwilioRestClient

import conf


def send(s):
    client.sms.messages.create(to=conf.TO, from_=conf.FROM, body=s)

# Use the first arg as the message to send, or use the default if not specified
default_message = "You haven't committed anything today!"
message = sys.argv[1] if len(sys.argv) > 1 else default_message

# Initialise twilio stuff
client = TwilioRestClient(conf.ACCOUNT_SID, conf.AUTH_TOKEN)

# Get Github contributions activity
url = 'https://github.com/users/%s/contributions_calendar_data' % conf.USERNAME
request = requests.get(url)
if request.ok:
    try:
        data = json.loads(request.text)

        # Get the number of commits made today
        commits_today = data[-1][1]

        if not commits_today:
            send(message)
    except:
        send('There was an error getting the number of commits today')
else:
    send('There was a problem accessing the Github API :(')
