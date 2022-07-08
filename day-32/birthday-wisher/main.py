##################### Extra Hard Starting Project ######################
import random
import smtplib
import datetime as dt
import pandas as pd
import os

MY_EMAIL = 'example.email@gmail.com'
MY_PASSWORD = 'abcdefgh'

# 1. Read the birthdays.csv
birthdays_df = pd.read_csv('birthdays.csv')
birthdays = birthdays_df.to_dict(orient='records')

# 2. Read the letter options from the letter templates folder
letter_folder = 'letter_templates'
letters = []
for file in os.listdir(letter_folder):
    file_path = os.path.join(letter_folder, file)
    with open(file_path) as f:
        letters.append(f.read())

# 3. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
for birthday in birthdays:
    if today.month == birthday['month'] and today.day == birthday['day']:
        # 4. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = random.choice(letters)
        letter = letter.replace("[NAME]", birthday['name'])

        # 5. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs=birthday['email'], 
                                msg=f"Subject:Happy Birthday!\n\n{letter}")