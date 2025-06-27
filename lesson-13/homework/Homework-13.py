from datetime import datetime, date
from dateutil.relativedelta import relativedelta

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
today = date.today()

rd = relativedelta(today, birth_date)

print(f"Your age: {rd.years} years, {rd.months} months, {rd.days} days.")


from datetime import datetime, date, timedelta

birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d").date()
today = date.today()

next_birthday = birth_date.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

delta = next_birthday - today

print(f"Days until next birthday: {delta.days}")

from datetime import datetime, timedelta

current_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
duration_hours = int(input("Enter meeting duration hours: "))
duration_minutes = int(input("Enter meeting duration minutes: "))

current_dt = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
end_dt = current_dt + timedelta(hours=duration_hours, minutes=duration_minutes)

print("Meeting will end at:", end_dt.strftime("%Y-%m-%d %H:%M"))



from datetime import datetime
import pytz

dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
from_tz_str = input("Enter your timezone (e.g., Europe/Berlin): ")
to_tz_str = input("Enter target timezone: ")

from_tz = pytz.timezone(from_tz_str)
to_tz = pytz.timezone(to_tz_str)

naive_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
from_dt = from_tz.localize(naive_dt)
to_dt = from_dt.astimezone(to_tz)

print("Converted datetime:", to_dt.strftime("%Y-%m-%d %H:%M (%Z)"))


from datetime import datetime
import time

future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
future_dt = datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    delta = future_dt - now
    if delta.total_seconds() <= 0:
        print("Countdown finished!")
        break
    print(f"Time remaining: {delta}")
    time.sleep(1)


import re

email = input("Enter email address: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
if re.match(pattern, email):
    print("Valid email.")
else:
    print("Invalid email.")


phone = input("Enter 10-digit phone number: ")

cleaned = re.sub(r'\D', '', phone)

if len(cleaned) == 10:
    formatted = f"({cleaned[:3]}) {cleaned[3:6]}-{cleaned[6:]}"
    print("Formatted phone number:", formatted)
else:
    print("Invalid phone number.")


import re

password = input("Enter password: ")

criteria = [
    (len(password) >= 8, "At least 8 characters"),
    (re.search(r'[A-Z]', password), "At least one uppercase letter"),
    (re.search(r'[a-z]', password), "At least one lowercase letter"),
    (re.search(r'\d', password), "At least one digit"),
]

all_met = True
for ok, desc in criteria:
    if ok:
        print(f"✔ {desc}")
    else:
        print(f"✘ {desc}")
        all_met = False

if all_met:
    print("Password is strong.")
else:
    print("Password is weak.")


text = """
This is a sample text. This text contains some words.
Feel free to search for any word in this text.
"""

word = input("Enter word to find: ")

positions = []
start = 0
while True:
    idx = text.find(word, start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + 1

print("Occurrences found at positions:", positions)



import re

text = input("Enter text: ")


pattern = r'\b(\d{4}-\d{2}-\d{2})\b|\b(\d{2}/\d{2}/\d{4})\b'

matches = re.findall(pattern, text)

dates = []
for m in matches:
    dates.extend([d for d in m if d])

print("Dates found:", dates)
