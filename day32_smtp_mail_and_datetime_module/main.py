import datetime as dt
import smtplib
import random
MY_EMAIL = "dom.olive.oil@gmail.com"
PASSWORD = "xohs ztal xwhr tukd"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:

    with open("quotes.txt") as quotes:
        quotes_list = quotes.readlines()
        day_quote = random.choice(quotes_list)
        quotes_list.remove(day_quote)

    # new connection to smtp protocol
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # encrypt protocol
        connection.starttls()

        # log in the email
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="mtr.oliveira.me@gmail.com",
                            msg=f"Subject:Motivational week quote\n\n{day_quote}")