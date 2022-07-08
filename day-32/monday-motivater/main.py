import smtplib
import datetime as dt
import random

now = dt.datetime.now()

if dt.datetime.weekday(now) == 0:
    with open('quotes.txt') as f:
        quotes = f.read().split('\n')

    random_quote = random.choice(quotes)

    my_email = 'example.email@gmail.com'
    my_password = 'abcdefgh'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs='example.email.second@yahoo.com', 
                            msg=f"Subject:Monday Motivation\n\n{random_quote}")