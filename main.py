from messages import kdrama_quotes
from messages import romantic_quotes

import random, schedule, time
from datetime import date

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number


def good_morning_message():
    # Twilio authorization
    account = twilio_account
    token = twilio_token
    client = Client(account, token)

    # Calculate days till August 15
    today = date.today()
    august_15 = date(2021, 8, 15)
    days_till_august_15 = august_15 - today

    quote = "Good morning kanye, {} days till I see you <3! - Ryan".format(days_till_august_15.days)
    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


def send_message(quotes_list):
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len(quotes_list) - 1)]

    client.messages.create(to=cellphone,
                           from_=twilio_number,
                           body=quote
                           )


# send a message at 3:00 AM EST
schedule.every().day.at("03:00").do(good_morning_message)

# send a message at 3:00 AM EST
schedule.every().day.at("03:00").do(send_message, romantic_quotes)

# send a message in 5:00 AM EST
schedule.every().day.at("05:00").do(send_message, kdrama_quotes)

# testing
# schedule.every().day.at("13:55").do(send_message, romantic_quotes)
schedule.every().day.at("16:16").do(good_morning_message)
schedule.every().day.at("16:16").do(good_morning_message)
schedule.every().day.at("16:16").do(good_morning_message)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
