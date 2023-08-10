import get_sunset
from datetime import datetime
from twitter.account import Account
from dotenv import load_dotenv
import os


load_dotenv()

EMAIL = os.getenv('EMAIL')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


def format_date(date):
    day = date.day

    def suffix(day):
        suffix = ""
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        return suffix

    return datetime.strftime(date, '%B %#d' + suffix(day) + ', %Y')

account = Account(EMAIL, USERNAME, PASSWORD)

sunset_time = get_sunset.get_sunset_time(51.5073509, -0.1277583, datetime.today().date())
written_date_today = format_date(datetime.today().date())
written_time = str(sunset_time.time())[:-3]

time_object = datetime.strptime(written_time, '%H:%M').time()
today_date = datetime.combine(datetime.today(), time_object).strftime('%Y-%m-%d %H:%M')
print(today_date, sunset_time)

text = f'Today is {written_date_today} and it is {written_time}. Have a good evening!'

account.schedule_tweet(text, today_date)




