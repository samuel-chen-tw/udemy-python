##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# 5. put the schedule on https://www.pythonanywhere.com/user/samuel3845/tasks_tab/

import datetime as dt
import smtplib
import pandas
import random

MY_EMAIL = "samuel811215@gmail.com"
MY_PASSWORD = "zrcusgixpsqhgwul"

# my solution

# now = dt.datetime.now()
# now.month
#
# birthdays_csv = pandas.read_csv("birthdays.csv")
# for index_month in birthdays_csv.month:
#     row_data = birthdays_csv[birthdays_csv['month'] == index_month]
#     if index_month == now.month and row_data.day.values[0] == now.day:
#         with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter:
#             letter_content = letter.read()
#             new_letter = letter_content.replace("[NAME]", row_data.name.values[0])
#             with smtplib.SMTP("smtp.gmail.com") as connection:
#                 connection.starttls()
#                 connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#                 connection.sendmail(
#                     from_addr=MY_EMAIL,
#                     to_addrs=row_data.email.values[0],
#                     msg=f"Subject:Happy Birthday\n\n{new_letter}"
#                 )

# Teacher solution
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
