import smtplib
import pandas
import random
import datetime as dt

MY_EMAIL = "samuel811215@gmail.com"
MY_PASSWORD = "zrcusgixpsqhgwul"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="Loman.Cheng@taiwanlife.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )



# import smtplib
#
# my_email = "samuel811215@gmail.com"
# password = "zrcusgixpsqhgwul"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="Loman.Cheng@taiwanlife.com",
#         msg="Subject:Hello\n\nHot dog didi")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
# date_of_birth = dt.datetime(year=1992, month=12, day=15)
# print(date_of_birth.weekday())







